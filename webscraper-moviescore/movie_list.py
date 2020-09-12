import pandas as pd


def make_list():
    xlsx = pd.read_excel("movie.xls")
    lists = xlsx.values.tolist()
    list = []
    for i in lists[4:]:
        list.append(i[1])
    return list
