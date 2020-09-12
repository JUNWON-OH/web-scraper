from jobs import brands_list, each_brand_info
from save import save_to_file

brand_list = brands_list()
infos = each_brand_info()
print(brand_list)
print(len(brand_list))
save_to_file(brand_list, infos)
