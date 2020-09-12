import csv
from naver_list import make_list
from imdb import imdb


def save_to_file(movies):
    file = open("imdb.csv", mode="w", encoding="utf-8", newline="")
    writer = csv.writer(file)
    writer.writerow(["Name", "Imdb"])
    for movie in movies:
        writer.writerow(list(movie.values()))
    return


movie_list = make_list()
print(movie_list)
save_to_file(imdb(movie_list))
