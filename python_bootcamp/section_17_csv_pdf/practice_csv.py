import csv

data = open('python_bootcamp/section_17_csv_pdf/example.csv', encoding='utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)

for line in data_lines[:6]:
    print(line)

all_emails = []
for line in data_lines[1:15]:
    all_emails.append(line[3])
print(all_emails)

full_names = []
for line in data_lines[1:15]:
    full_names.append(line[1] + " " + line[2])
print(full_names)

data.close()


file_to_output = open('python_bootcamp/section_17_csv_pdf/to_save_file.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(file_to_output, delimiter=',')
csv_writer.writerow(['a', 'b', 'c'])
csv_writer.writerows([['1', '2', '3'], ['4', '5', '6']])
file_to_output.close()


f = open('python_bootcamp/section_17_csv_pdf/to_save_file.csv', 'a', newline='', encoding='utf-8')
csv_writer = csv.writer(f)
csv_writer.writerow(['new', 'new', 'new'])
f.close()
