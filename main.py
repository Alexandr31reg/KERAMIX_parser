import json
import requests
from bs4 import BeautifulSoup


def get_first_news():
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/117.0"
    }

    url = "https://keramix-oskol.ru/catalog/tekhnopleks/"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    articles_card = soup.find_all("div", class_="catalog-item-info")

    news_dict = {}
    for article in articles_card:
        article_title = article.find(
            "div", class_="item-all-title").text.strip()
        article_desc = article.find("div", class_="article").text.strip()
        article_price = article.find("div", class_="item-price").text.strip()
        all_a = article.find_all("a", class_="item-title")
        for item in all_a:
            item_text = item.text.strip()
            item_href = "https://keramix-oskol.ru" + item.get("href")

        article_id = item_href.split("/")[-2]

        news_dict[article_id] = {
            "article_title": article_title,
            "article_desc": article_desc,
            "article_price": article_price,
            "article_url": item_href
        }

    with open("news_dict.json", "w") as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)


def main():
    get_first_news()


if __name__ == '__main__':
    main()
