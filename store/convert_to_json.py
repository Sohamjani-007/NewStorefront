import xlrd
from collections import OrderedDict
import json

wb = xlrd.open_workbook("/home/oto/Downloads/video_reviews.xlsx")
ws = wb.sheet_by_index(0)

data_list = []
for rownum in range(1, ws.nrows):
    data = OrderedDict()

    row_values = ws.row_values(rownum)
    data['id'] = row_values[0]
    data['created'] = row_values[1]
    data_list.append(data)
    print(data)
    with open("RulesJson.json", "w", encoding="utf-8") as writeJsonfile:
        json.dump(data_list, writeJsonfile, indent=4,default=str) 
