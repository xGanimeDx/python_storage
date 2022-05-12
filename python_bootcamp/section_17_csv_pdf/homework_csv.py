import csv

data = open('python_bootcamp/section_17_csv_pdf/find_the_link.csv', 'r', encoding='utf-8')
data_lines = list(data)
url = ''

for row_num, data in enumerate(data_lines):
    url += data[row_num]

print(url)