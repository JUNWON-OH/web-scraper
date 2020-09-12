import pandas as pd


def make_list():
    xlsx = pd.read_csv("naver.csv")
    lists = xlsx.values.tolist()
    english_list = []
    for i in lists:
        english_list.append({"English": i[1], "English for research": i[3]})
    return english_list
