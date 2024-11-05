from .selenium_url import curl
from .crawl_product import get_all_data, get_neccesary_data
import concurrent.futures


import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SEARCH_DOMAIN = "https://{}/api/v4/search/search_items?by=relevancy&extra_params=%7B%22global_search_session_id%22%3A%22gs-2800b18f-4814-431d-9c14-51baf573b365%22%2C%22search_session_id%22%3A%22ss-77a7d1ef-0f18-4936-bb9e-6b5613ee1937%22%7D&keyword={}&limit=60&newest=0&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2&view_session_id=8b96927b-80c7-4a79-8647-85e56b6029e9"

def get_total(origin, keyword):
    url = SEARCH_DOMAIN.format(origin, keyword)
    print("DEBUG", curl(url))

    return curl(url)['total_count']

def get_keyword_encoded(keyword):
    return "%20".join(key for key in keyword.split())

def crawl_by_search(origin, keyword:str, limit:int=60, max_workers:int=32) -> list:

    temp = get_keyword_encoded(keyword=keyword)

    total_count = get_total(origin, temp)
    logger.info(f"There are {total_count} products in \"{keyword}\"")
    futures = []
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        for newest in range(0, total_count, limit):
            url = SEARCH_DOMAIN.format(origin, temp, limit, newest)
            futures.append(executor.submit(get_all_data, url))

    for future in concurrent.futures.as_completed(futures):
        results.extend(future.result())
        
    all_data = get_neccesary_data(origin, results)
    length = len(all_data)
    if length == total_count:
        logger.info(f"Successfully crawl all {total_count} products from \"{keyword}\"")
    elif length < total_count:
        logger.info(f"Successfully crawl {length} products from \"{keyword}\"")

    return all_data