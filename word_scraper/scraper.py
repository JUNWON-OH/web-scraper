import requests
from bs4 import BeautifulSoup


def get_last_page(rank):
    URL = f"https://learn.dict.naver.com/m/cndic/wordbook/hsk/10{rank}/20{rank}/words.nhn?filterType=0&orderType=2&pageNo=1"
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = (
        soup.find("div", {"id": "header"})
        .find("div", {"class": "u_pg2"})
        .find("span", {"class": "u_pg2_total"})
        .get_text(strip=True)
    )
    last_page = pages.replace("/", "").lstrip()

    return last_page


def get_words(pages, rank):
    word_list = []
    for page in range(pages):
        page += 1
        print("Scraping page : ", page)
        URL = f"https://learn.dict.naver.com/m/cndic/wordbook/hsk/10{rank}/20{rank}/words.nhn?filterType=0&orderType=2&pageNo={page}"
        result = requests.get(URL)
        soup = BeautifulSoup(result.text, "html.parser")
        words = (
            soup.find("div", {"id": "header"})
            .find("div", {"class": "t_content"})
            .find("ul", {"class": "entryLayer"})
            .find_all("li")
        )
        for word in words:
            china = word.find("p").find("a").get_text(strip=True)
            pure_korea = word.find("p", {"class": "txt_ct2"}).get_text(strip=True)
            korea = "".join(pure_korea.split())
            word_list.append({"china": china, "korea": korea})

    return word_list

