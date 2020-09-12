import requests
from bs4 import BeautifulSoup


def save_link(lists):
    movie_links = []
    for movie in lists:
        try:
            link = f"http://movie.naver.com/movie/search/result.nhn?query={movie}&section=all&ie=utf8"
            result = requests.get(link)
            soup = BeautifulSoup(result.text, "html.parser")
            movie_soup = (
                soup.find("ul", {"class": "search_list_1"}).find("dt").find("a")["href"]
            )
            movie_link = f"http://movie.naver.com{movie_soup}"
            movie_links.append({"Name": movie, "Link": movie_link})
        except:
            movie_links.append({"Name": movie, "Link": "Error"})
    return movie_links


def score(links):
    movie_score = []
    for link in links:
        try:
            print("Scrapping from Naver : ", link["Name"])
            movie_link = link["Link"]
            result = requests.get(movie_link)
            soup = BeautifulSoup(result.text, "html.parser")
            english = (
                soup.find("div", {"class": "mv_info"})
                .find("h3", {"class": "h_movie"})
                .find("strong")
                .get_text(strip=True)
            )
            english_list = str(english).split(",")
            try:
                english_name = english_list[-2].rstrip().lstrip()
                year = english_list[-1].lstrip().rstrip()
                english_search = english_name + "_" + year
            except:
                english_name = ""
                year = english_list[-1].lstrip().rstrip()
                english_search = ""

            score_netizen = (
                soup.find("div", {"class": "score_area"})
                .find("div", {"class": "netizen_score"})
                .find("div", {"class": "star_score"})
                .find("em")
                .get_text()
            )
            score_special = (
                soup.find("div", {"class": "score_area"})
                .find("div", {"class": "special_score"})
                .find("div", {"class": "star_score"})
                .find("em")
                .get_text(strip=True)
            )
            movie_score.append(
                {
                    "Nme": link["Name"],
                    "English": english_name,
                    "Year": year,
                    "English for search": english_search,
                    "Netizen": score_netizen,
                    "Special": score_special,
                }
            )
        except:
            print("Scrapping from Naver : ", link["Name"], " ERROR")
            movie_score.append(
                {
                    "Nme": link["Name"],
                    "English": "",
                    "Year": "",
                    "English for search": "",
                    "Netizen": "",
                    "Special": "",
                }
            )
    return movie_score
