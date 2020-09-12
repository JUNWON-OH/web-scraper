import csv
from movie_list import make_list
from naver import score, save_link


def save_to_file(movies):
    file = open("naver.csv", mode="w", encoding="utf-8", newline="")
    writer = csv.writer(file)
    writer.writerow(
        ["Name", "English", "Year", "English for search", "Netizen", "Special"]
    )
    for movie in movies:
        writer.writerow(list(movie.values()))
    return


lists = make_list()
links = save_link(lists)
movie_score = score(links)
print(movie_score[1]["Year"])
save_to_file(movie_score)
