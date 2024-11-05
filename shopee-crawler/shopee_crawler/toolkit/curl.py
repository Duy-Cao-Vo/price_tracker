import requests
import random
import time

def get_header():
    return {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Content-Type': 'application/json',
        'X-API-Source': 'pc',
        'X-CSRFToken': 'QBAdpym9FCIIrABNEM6upWWg4VT8ae8s',
        'X-Requested-With': 'XMLHttpRequest',
        'X-SAP-RI': 'c0e328670cec64aa5334213505013fe03cc40a584a5fa1d58d19',
        'X-SAP-SEC': 'mqazCM/C4sbspfCIpsCIpHBITsYOpoOIcnGvponIVsCypsCIXsCOpEsIhsCvpHsIcKGOpHQI+sYWphWIrsYppHCINCYBpelIcsYVpHWILCCtpOxIIsYEpp/IvnY4phKIsCGupEfIBsCapPlI4sG7pOlIHsYkprfI5sGSpeQIWsGBprxI/sY/phsIcnCIpH9e2nFerLoPpsCItVn4psCIphWdvsfIp5C4psY9v4+o8sfIpEi0kDCInR2YHnzZTKK5psCIVK0yaCRw1KCIeDUxpnCIpswQAEn4psCIpsYGHsxIpsCIYNBQpKCIpsCIpxC4psYlpnCIHHDI8q5r7CQIpO29YKb5e327z0OIxBmcNCqnLdsIpsCIpsYXgvQI67ue7P7EpnCIpswCGGnIpsYspnCIpsCIqh/xc8DILJzK8KCIpIpiig0MYCpSNusQDzoilNZjxyeOTdBxTpjWZxwmcIeCBzbcXzyDM5UUcFPG0QvGmJAijmg2xJgyWMdPO/I9RQBD/atyZZBC2tMtKvEIRaUnS3b2iAmqDZBxCgJa/kCxtXJcNZCAwU/oo4UFc3ZY8coJSN4rWRSCZxoAe+GamErWwn9mVpOMSmkleNXLuQz8hxFRENJyT3nfKCqiOkaT0oIZF6zrAvOQXgsIpsCOpsCIqvpvfKnIpsCsdLBMhnxIpPBKKhU1XCqB/l7xB4GJGlU5psSt5izWrCSbeziEsl23m82R2APIEVAm1Xh0B0ZxL6kUJArLabE2Z1JN/tgHy1h0toSh4Cead6UYRW29drBkTsujUfvvKbkf8EbEeJSrVZ68cvj6Drr5jez6gSCcTCjHpQ04cEDWQIKsHCwff1F9eWfW8+qZMtHIdTg0aQFN72qFFf05TOH9hEAcM5/k8kolhnC+8bEa8xYoiL3TiROxYJizX4zpSeEBXf2lnXOb5TVZ2seszis9dgLzykCRI+0rRmWj7qTxlXiaMR4djPHMFlxVFq76lJdXNFW5X7ABBnr7tplu6ToPhb32FQsERNCXe4EyGkvb1i0UpsCEpsCI1d68374QnsxopsCIxLda08ixsbu/EjMPVNBIps/IpsY72RQrYTOp5ODIpsCIpsCIpsCIps/IpsY72RQrYTOp5ODIpsCxpsCIZ/4WKlw12oz2EkDMYTJ4Qm3EX/iRD/C8xx+XSPizHVw0EzxBUyEdRcCL9L1+DvgzbhHy0gNvHqlIpsCIhsCIpI7JOBCmtqZkpnCIpPgBpsCEpsCIJ2vf4pF8JpnIpsCIhsCIp4/U1HTAtYZkhsCIpSnj41ly47ljpsCIps==',
        'X-Shopee-Language': 'vi',
        'X-SZ-SDK-Version': '1.12.5'
    }

def get_cookies():
    cookies_str = "_QPWSDCXHZQA=82f941d7-7574-4c1e-c7ae-96f643ba2cab; REC7iLP4Q=8d1f3ebe-b065-4baf-a071-b005059ea3fc; REC_T_ID=26387589-99bd-11ef-b1d3-eef56494ab45; SPC_SI=XX7yZgAAAAAxY1ZCdlk1RQXInQMAAAAAeGFpODMwblA=; SPC_F=JwpCjrCed0aTmADeVaJBZ9BpmrUY3cEd; SPC_CLIENTID=SndwQ2pyQ2VkMGFUpzftizurndwwpfmi; SPC_EC=.clE3cWdYZjhKT0E3Sms3ej8r4c48M3KWS7YwnF8oLKL2bLA8SerReIPIaL1nMh2ADUd2VW2jFEGCi2lG0hOujhjo+tRWEZWHXoSs2DU8euHYy8dhV6KLF8baxWaY+g+F7DQgikPPUPOJAyhonFwpZyqlncP0OsPXvzNZsto+b9QXAeON59bNEgRDX+gM3jAN0XsCreF8Pg4EhGBI3b72ZR5elgawpv1afF+LX8F6SJs=; SPC_ST=.clE3cWdYZjhKT0E3Sms3ej8r4c48M3KWS7YwnF8oLKL2bLA8SerReIPIaL1nMh2ADUd2VW2jFEGCi2lG0hOujhjo+tRWEZWHXoSs2DU8euHYy8dhV6KLF8baxWaY+g+F7DQgikPPUPOJAyhonFwpZyqlncP0OsPXvzNZsto+b9QXAeON59bNEgRDX+gM3jAN0XsCreF8Pg4EhGBI3b72ZR5elgawpv1afF+LX8F6SJs=; SPC_U=82899251; SPC_R_T_ID=jL5k5mTfU5kY0u3i1UNgGhLGo67V9WILdvfUDzdwKCSels/tYFWmNZXcbzwaE8jQfObDJ+FRKJWRe6uDSKBJgOpx8+tCpW4T0zVwbyFd/XGe+8mXYFj+VQVvkaUq81EvmcQPDC435uej/Zqih+u6WuaveHLuDzlf/Lpm1T9xO2o=; SPC_R_T_IV=QXluaXBudHA3TERsQkpOYw==; SPC_T_ID=jL5k5mTfU5kY0u3i1UNgGhLGo67V9WILdvfUDzdwKCSels/tYFWmNZXcbzwaE8jQfObDJ+FRKJWRe6uDSKBJgOpx8+tCpW4T0zVwbyFd/XGe+8mXYFj+VQVvkaUq81EvmcQPDC435uej/Zqih+u6WuaveHLuDzlf/Lpm1T9xO2o=; SPC_T_IV=QXluaXBudHA3TERsQkpOYw==; __LOCALE__null=VN; csrftoken=QBAdpym9FCIIrABNEM6upWWg4VT8ae8s; _sapid=0f08caae653bedc90a5506ac6c3c183676ec8f37941b55c594f09c3e; SPC_SEC_SI=v1-SUh6QkQxRWpOM3NkQTdKeEJclGPI51W1uZq3oGj+s6XWNuKOXj4QcvbjaDG11PQcqBJ5zMuDRaE+R0FuJt9kD9VK/716FSsWR+iZ/ek2+1c=; SPC_IA=1; SPC_CDS_CHAT=de862b80-cbfb-4c02-ba49-535ef95db069; AC_CERT_D=U2FsdGVkX185WZOcQu+mEYyrPdCC3TSkE0BNXMny5l4qkJFJcsnTFNkcfirM8UJ/7bIWEPrcw1JDeyMd7DD40tMqCKrX65yglPO2jDKZflx5jl01TXfE/7YzA810qswuWtOTrDvVu8/0Y1pTVzCd/lrXVKdGg1uK10cvrNdAzmU3o3WkmaChQqtO98Elysutu3I2kb9FsGKtzWh1+VVR9IIJNL6e4REuR9GA7WETSpZ8PFgGYir+P8lQ0umqvs38Fyvr8fuES7uErrptZpGj+w8G9YlCtkZiNI1liEsY0KPLJ/1lZDu4MXbGqp2fWGFymJOpDuyAvSrXgPRSul9ZLYLhycCO6V1v6LkXTU9Nzg77DYmOHOuPy6uZPN72TI8VBgKp4yscm8oNeIAg150fnA5PANGRZxBYN/QLccLjgTVJ9hvya3XKB/DziDTX5qCQ9HIOkDPHBdoUfz2Q+v6Mz99VI2n2k00oG3Ns5mhnBViyLedK+jpwD142UaztLOFU4YciIBNPlvZutH5mlwkKdMXX0flhxeqgRqOYwYtr3icUQn4Hyo4DHEhxf7YCDWEmqP+6QgcKodH3BVfj3jslQme2KjSEQu0EORNpkxEa2kN2IKsRrWa/cdXwEsqwidgTKeueRl06uLZ15LyBdMGU3gJ7lFEJExPQkbCniUMXBfys9cMd412Mth0GAh5Zr6Ee58NMf/tRlCYdt4YRd7T+KrXhg9TAknaHjTDA+3Gh6fEaN7ZJf67aAp2OFgyUlPNvA3TF9MaQowi8Qf5rJmAaE6fW1r7mPoFmlx1WdGDk9Hh5yDqxPF8N5LC1ocpk+DViJXgW6ekDon1iX9qvxNGQBakwCTWJrgDDwpyNvhjNoAvijcBUO8iVFnm0acr/iEnuMo7wbeMUaSNdN9exBCTkPhuLGqVQz+gZxaDDYxCHGIatgHQuMMxFlwIYGLWelv8taorjWAfaH7CfqcQOlOzYQfLt47Q1yP0+oo4bVYy4EnAKTprzbpjxvmBJwY1nTtc4v7n+qwQnCCNmwRDUBrcAggLP7WXFrJe5/ecLe53oJkhOSgKyWGEvIPRZLdnr0anWYaS2tl5eJcf0kl3kKFfU+esqsHdiLhRpJAVfOz80BYE="
    cookies = {}
    for cookie in cookies_str.split('; '):
        key, value = cookie.split('=', 1)
        cookies[key] = value
    return cookies

def retry_with_backoff(retries=3, backoff_in_seconds=1):
    def rwb(func):
        def wrapper(url):
            x = 0
            while True:
                try:
                    return func(url)
                except:
                    if x == retries:
                        raise
                    else:
                        sleep = (backoff_in_seconds * 2 ** x +
                                 random.uniform(0, 1))
                        time.sleep(sleep)
                        x += 1
        return wrapper
    return rwb

@retry_with_backoff()
def curl(url: str, timeout: int=10) -> dict:
    print("DEBUG", url)
    response = requests.get(
        url,
        headers=get_header(),
        cookies=get_cookies(),
        timeout=timeout
    )
    return response.json()