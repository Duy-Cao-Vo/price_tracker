from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import requests
from bs4 import BeautifulSoup
from datetime import datetime

from utils import mkdir_if_not_exist
import os

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    track_date = Column(DateTime, default=datetime.utcnow)
    source = Column(String)
    rating = Column(Float)
    relevant_products = Column(String)  # JSON string

Base.metadata.create_all(bind=engine)

class ProductCreate(BaseModel):
    name: str
    price: float
    track_date: datetime
    source: str
    rating: float
    relevant_products: List[dict]

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("static/index.html") as f:
        return f.read()

import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/product")
def get_product_info(url: str):
    # try:
    if True:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        soup = BeautifulSoup(response.content, 'html.parser')

        mkdir_if_not_exist('craw')

        # Save HTML content to a file for debugging
        html_file_path = os.path.join('craw', 'product_page.html')
        with open(html_file_path, 'w', encoding='utf-8') as file:
            file.write(response.text)

        # Extract product details with error handling
        name_tag = soup.find('div', {'class': 'WBVL_7'}) # product name
        price_tag = soup.find('div', {'class': 'IZPeQz B67UQ0'}) # product price
        rating_tag = soup.find('div', {'class': 'F9RHbS dQEiAI jMXp4d'}) # product rating

        if not name_tag or not price_tag or not rating_tag:
            raise ValueError("Required product details not found on the page")

        name = name_tag.text
        price = float(price_tag.text.replace('₫', '')) #₫105.000
        rating = float(rating_tag.text)
        relevant_products = []  # Add logic to find relevant products

        print("DEBUG")
        print(name)
        print(price)
        print(rating)

        product = ProductCreate(
            name=name,
            price=price,
            track_date=datetime.now(),
            source=url,
            rating=rating,
            relevant_products=relevant_products
        )

        db = SessionLocal()
        db_product = Product(
            name=product.name,
            price=product.price,
            track_date=product.track_date,
            source=product.source,
            rating=product.rating,
            relevant_products=str(product.relevant_products)
        )
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        db.close()

        return product
    # except requests.RequestException as e:
    #     logger.error(f"Request error: {e}")
    #     raise HTTPException(status_code=500, detail="Error fetching the product page")
    # except ValueError as e:
    #     logger.error(f"Parsing error: {e}")
    #     raise HTTPException(status_code=500, detail=str(e))
    # except Exception as e:
    #     logger.error(f"Unexpected error: {e}")
    #     raise HTTPException(status_code=500, detail="An unexpected error occurred")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



import time
from shopee_crawler import Crawler

crawler = Crawler()
crawler.set_origin(origin="shopee.vn")

keyword = 'điện thoại samsung'

# Start time
start = time.time()

# Crawl
data = crawler.crawl_by_shop_url(shop_url='https://shopee.vn/phuc09999?categoryId=100535&entryPoint=ShopByPDP&itemId=21700788718')

# End time
end = time.time()

# Time crawling
print("Time : ",end - start, "seconds")