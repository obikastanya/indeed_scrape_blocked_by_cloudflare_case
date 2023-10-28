import cloudscraper
from fake_useragent import UserAgent

import config

ua = UserAgent()

user_agent = ua.random

url = f"{config.HOST}/jobs"
params = {"radius": 100, "l": "United States", "q": "Accountant", "start": 0}

proxies = {"http": config.PROXIES[0]}
headers = {"User-Agent": user_agent}


def test_connection():
    scraper = cloudscraper.create_scraper(disableCloudflareV1=True)

    response = scraper.get(url=url, params=params, proxies=proxies, headers=headers)

    print(response.status_code)

    if response.status_code != 200:
        filename = f"{response.status_code}.html"

        with open(filename, "w", encoding="utf-8") as file:
            file.write(response.text)


if __name__ == "__main__":
    test_connection()
