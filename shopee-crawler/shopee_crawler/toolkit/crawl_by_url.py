# crawl_by_url.py
from .selenium_url import curl
from .crawl_product import get_all_data, get_neccesary_data
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def crawl_by_url(origin, url: str) -> list:
    # Fetch data using Selenium
    data = curl(url)

    # Process the fetched data
    all_data = get_neccesary_data(origin, data['items'])

    # Log the number of products fetched
    logger.info(f"Successfully fetched {len(all_data)} products from the URL.")

    return all_data


# Example usage
if __name__ == "__main__":
    url = "https://shopee.vn/api/v4/search/search_items?by=relevancy&keyword=%C4%91i%E1%BB%87n%20tho%E1%BA%A1i%20samsung&limit=60&newest=0&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2"
    all_data = crawl_by_url('shopee.vn',url)
    print(all_data)
