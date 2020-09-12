import csv


def save_to_file(brands, infos):
    for brand in brands:
        print(brand)
        file = open(f"{brand}.csv", mode="w", encoding="utf-8", newline='')
        writer = csv.writer(file)
        writer.writerow(['Place', 'Company', 'Title', 'Time', 'Pay'])
        for info_list in infos[brand]:
            writer.writerow(list(info_list.values()))
