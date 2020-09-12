import requests
from bs4 import BeautifulSoup


def rotten(movies):
    rotten = []
    for movie in movies:
        print("Scrapping from rotten : ", movie["English"])
        try:
            movie_english = str(movie["English for research"])
            movie_search = (
                movie_english.replace(" ", "_")
                .replace(":", "")
                .replace("_-_", "_")
                .lower()
            )
            print(movie_search)
            URL = f"https://www.rottentomatoes.com/m/{movie_search}"
            result = requests.get(URL)
            soup = BeautifulSoup(result.text, "html.parser")
            pre_score = soup.find("div", {"class": "score-panel-wrap"}).find(
                "section", {"class": "mop-ratings-wrap__row"}
            )
            try:
                score = (
                    pre_score.find("a", {"href": "#contentReviews"})
                    .find("span", {"class": "mop-ratings-wrap__percentage"})
                    .get_text(strip=True)
                )
                rotten.append({"Name": movie_search, "rotten": score})
            except:
                print("except")
                score = "0%"
                rotten.append({"Name": movie_search, "rotten": score})
        except:
            print("except")
            try:
                movie_english = str(movie["English"])
                movie_search = (
                    movie_english.replace(" ", "_")
                    .replace(":", "")
                    .replace("_-_", "_")
                    .lower()
                )
                URL = f"https://www.rottentomatoes.com/m/{movie_search}"
                result = requests.get(URL)
                soup = BeautifulSoup(result.text, "html.parser")
                pre_score = soup.find("div", {"class": "score-panel-wrap"}).find(
                    "section", {"class": "mop-ratings-wrap__row"}
                )
                try:
                    score = (
                        pre_score.find("a", {"href": "#contentReviews"})
                        .find("span", {"class": "mop-ratings-wrap__percentage"})
                        .get_text(strip=True)
                    )
                    rotten.append({"Name": movie_search, "rotten": score})
                except:
                    print("except")
                    score = "0%"
                    rotten.append({"Name": movie_search, "rotten": score})
            except:
                print("except")
                score = "None"
                rotten.append({"Name": movie_search, "rotten": score})

    return rotten
