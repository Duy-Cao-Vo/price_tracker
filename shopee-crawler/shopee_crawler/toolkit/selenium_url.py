# selenium_curl.py
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def get_cookies():
    cookies_str = "_QPWSDCXHZQA=82f941d7-7574-4c1e-c7ae-96f643ba2cab; REC7iLP4Q=8d1f3ebe-b065-4baf-a071-b005059ea3fc; REC_T_ID=26387589-99bd-11ef-b1d3-eef56494ab45; SPC_SI=XX7yZgAAAAAxY1ZCdlk1RQXInQMAAAAAeGFpODMwblA=; SPC_F=JwpCjrCed0aTmADeVaJBZ9BpmrUY3cEd; SPC_CLIENTID=SndwQ2pyQ2VkMGFUpzftizurndwwpfmi; SPC_EC=.clE3cWdYZjhKT0E3Sms3ej8r4c48M3KWS7YwnF8oLKL2bLA8SerReIPIaL1nMh2ADUd2VW2jFEGCi2lG0hOujhjo+tRWEZWHXoSs2DU8euHYy8dhV6KLF8baxWaY+g+F7DQgikPPUPOJAyhonFwpZyqlncP0OsPXvzNZsto+b9QXAeON59bNEgRDX+gM3jAN0XsCreF8Pg4EhGBI3b72ZR5elgawpv1afF+LX8F6SJs=; SPC_ST=.clE3cWdYZjhKT0E3Sms3ej8r4c48M3KWS7YwnF8oLKL2bLA8SerReIPIaL1nMh2ADUd2VW2jFEGCi2lG0hOujhjo+tRWEZWHXoSs2DU8euHYy8dhV6KLF8baxWaY+g+F7DQgikPPUPOJAyhonFwpZyqlncP0OsPXvzNZsto+b9QXAeON59bNEgRDX+gM3jAN0XsCreF8Pg4EhGBI3b72ZR5elgawpv1afF+LX8F6SJs=; SPC_U=82899251; SPC_R_T_ID=jL5k5mTfU5kY0u3i1UNgGhLGo67V9WILdvfUDzdwKCSels/tYFWmNZXcbzwaE8jQfObDJ+FRKJWRe6uDSKBJgOpx8+tCpW4T0zVwbyFd/XGe+8mXYFj+VQVvkaUq81EvmcQPDC435uej/Zqih+u6WuaveHLuDzlf/Lpm1T9xO2o=; SPC_R_T_IV=QXluaXBudHA3TERsQkpOYw==; SPC_T_ID=jL5k5mTfU5kY0u3i1UNgGhLGo67V9WILdvfUDzdwKCSels/tYFWmNZXcbzwaE8jQfObDJ+FRKJWRe6uDSKBJgOpx8+tCpW4T0zVwbyFd/XGe+8mXYFj+VQVvkaUq81EvmcQPDC435uej/Zqih+u6WuaveHLuDzlf/Lpm1T9xO2o=; SPC_T_IV=QXluaXBudHA3TERsQkpOYw==; __LOCALE__null=VN; csrftoken=QBAdpym9FCIIrABNEM6upWWg4VT8ae8s; _sapid=0f08caae653bedc90a5506ac6c3c183676ec8f37941b55c594f09c3e; SPC_SEC_SI=v1-SUh6QkQxRWpOM3NkQTdKeEJclGPI51W1uZq3oGj+s6XWNuKOXj4QcvbjaDG11PQcqBJ5zMuDRaE+R0FuJt9kD9VK/716FSsWR+iZ/ek2+1c=; SPC_IA=1; SPC_CDS_CHAT=de862b80-cbfb-4c02-ba49-535ef95db069; AC_CERT_D=U2FsdGVkX185WZOcQu+mEYyrPdCC3TSkE0BNXMny5l4qkJFJcsnTFNkcfirM8UJ/7bIWEPrcw1JDeyMd7DD40tMqCKrX65yglPO2jDKZflx5jl01TXfE/7YzA810qswuWtOTrDvVu8/0Y1pTVzCd/lrXVKdGg1uK10cvrNdAzmU3o3WkmaChQqtO98Elysutu3I2kb9FsGKtzWh1+VVR9IIJNL6e4REuR9GA7WETSpZ8PFgGYir+P8lQ0umqvs38Fyvr8fuES7uErrptZpGj+w8G9YlCtkZiNI1liEsY0KPLJ/1lZDu4MXbGqp2fWGFymJOpDuyAvSrXgPRSul9ZLYLhycCO6V1v6LkXTU9Nzg77DYmOHOuPy6uZPN72TI8VBgKp4yscm8oNeIAg150fnA5PANGRZxBYN/QLccLjgTVJ9hvya3XKB/DziDTX5qCQ9HIOkDPHBdoUfz2Q+v6Mz99VI2n2k00oG3Ns5mhnBViyLedK+jpwD142UaztLOFU4YciIBNPlvZutH5mlwkKdMXX0flhxeqgRqOYwYtr3icUQn4Hyo4DHEhxf7YCDWEmqP+6QgcKodH3BVfj3jslQme2KjSEQu0EORNpkxEa2kN2IKsRrWa/cdXwEsqwidgTKeueRl06uLZ15LyBdMGU3gJ7lFEJExPQkbCniUMXBfys9cMd412Mth0GAh5Zr6Ee58NMf/tRlCYdt4YRd7T+KrXhg9TAknaHjTDA+3Gh6fEaN7ZJf67aAp2OFgyUlPNvA3TF9MaQowi8Qf5rJmAaE6fW1r7mPoFmlx1WdGDk9Hh5yDqxPF8N5LC1ocpk+DViJXgW6ekDon1iX9qvxNGQBakwCTWJrgDDwpyNvhjNoAvijcBUO8iVFnm0acr/iEnuMo7wbeMUaSNdN9exBCTkPhuLGqVQz+gZxaDDYxCHGIatgHQuMMxFlwIYGLWelv8taorjWAfaH7CfqcQOlOzYQfLt47Q1yP0+oo4bVYy4EnAKTprzbpjxvmBJwY1nTtc4v7n+qwQnCCNmwRDUBrcAggLP7WXFrJe5/ecLe53oJkhOSgKyWGEvIPRZLdnr0anWYaS2tl5eJcf0kl3kKFfU+esqsHdiLhRpJAVfOz80BYE="
    cookies = {}
    for cookie in cookies_str.split('; '):
        key, value = cookie.split('=', 1)
        cookies[key] = value
    return cookies

def get_header():
    return {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'Accept': 'application/json',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'X-Requested-With': 'XMLHttpRequest',
        'X-Shopee-Language': 'vi',
        'X-SZ-SDK-Version': '1.12.5'
    }

def save_html_to_file(html_content, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)

def curl(url: str, timeout: int=10) -> dict:
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    driver.get(url)

    # Add cookies to the browser
    for name, value in get_cookies().items():
        driver.add_cookie({'name': name, 'value': value})

    # Refresh the page to apply cookies
    driver.refresh()

    # Wait for the page to load
    time.sleep(timeout)

    # Get the page source
    html_content = driver.page_source

    # Save the HTML content to a file
    if not os.path.exists('./tmp'):
        os.makedirs('./tmp')
    file_path = './tmp/page.html'
    save_html_to_file(html_content, file_path)

    # Close the browser
    driver.quit()

    # Parse the HTML content using BeautifulSoup
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    return soup

# Example usage
if __name__ == "__main__":
    url = "https://shopee.vn/api/v4/search/search_items?by=relevancy&keyword=%C4%91i%E1%BB%87n%20tho%E1%BA%A1i%20samsung&limit=60&newest=0&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2"
    response = curl(url)
    print(response.prettify())