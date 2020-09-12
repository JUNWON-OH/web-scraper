import csv
from scraper import get_last_page, get_words


def save_to_file(word_list):
    file = open("words.csv", mode="w", encoding="utf-8", newline="")
    writer = csv.writer(file)
    writer.writerow(["china", "korea"])
    for word in word_list:
        writer.writerow(list(word.values()))
    return


page = int(get_last_page(6))
word_list = get_words(page, 6)
save_to_file(word_list)
