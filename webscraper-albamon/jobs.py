import requests
from bs4 import BeautifulSoup

URL = "http://www.alba.co.kr"


def each_info(link):
    result = requests.get(link)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find("div", {"id": "NormalInfo"}).find(
        "table").find("tbody").find_all("tr")
    real_results = []
    each_info = []
    for result in results:
        try:
            if result["class"] != ['summaryView']:
                real_results.append(result)
            for real_result in real_results:
                place = real_result.find(
                    "td", {"class": "local"}).get_text().replace('&nbsp', ' ')
                company = real_result.find("td", {"class": "title"}).find(
                    "span", {"class": "company"}).get_text()
                title = real_result.find("td", {"class": "title"}).find(
                    "span", {"class": "title"}).get_text()
                time = real_result.find("td", {"class": "regDate"}).get_text()
                pay = real_result.find("td", {"class": "pay"}).get_text()
                each_info.append({'Place': place, 'Company': company,
                                  'Title': title, 'Time': time, 'Pay': pay})
        except:
            each_info.append({'Place': '', 'Company': '',
                              'Title': '', 'Time': '', 'Pay': ''})
    return each_info


def brands_info(infos):
    brand_info = {}
    for info in infos:
        brand_name = info["Name"]
        brand_link = info["Link"]
        brand_info[brand_name] = each_info(brand_link)
    return brand_info


def get_brands(htmls):
    brand_info = []
    for html in htmls:
        html_class = html.find("a", {"class": "brandHover"})
        if "multi" in html_class["class"]:
            brands = html.find_all("a", {"class": "brandHover"})
            for brand in brands:
                brand_name = brand.find(
                    "span", {"class": "company"}).find("strong").get_text(strip=True)
                brand_link = brand["href"]
                brand_info.append({"Name": brand_name, "Link": brand_link})
        else:
            brand_name = html_class.find(
                "span", {"class": "company"}).find("strong").get_text(strip=True)
            brand_link = html_class["href"]
            brand_info.append({"Name": brand_name, "Link": brand_link})
    return brand_info


def alba_soup():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    superbrands = soup.find("div", {"id": "MainSuperBrand"}).find("ul", {"class": "goodsBox"}).find_all(
        "li", {"class": "impact"})
    return superbrands


brands = get_brands(alba_soup())


def brands_list():
    brand_list = []
    for brand in brands:
        brand_list.append(brand['Name'])
    return brand_list


def each_brand_info():
    return brands_info(brands)
