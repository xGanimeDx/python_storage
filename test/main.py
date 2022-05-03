import zipfile
import os
import re

zip_obj = zipfile.ZipFile('test/unzip_me_for_instructions.zip', 'r')
zip_obj.extractall('test/new')

with open('test/new/extracted_content/Instructions.txt', 'r', encoding='utf-8') as f:
    print(f.read())

folders_list = ['One', 'Two', 'Three', 'Four', 'Five']

pattern = r"\d{3}-\d{3}-\d{4}"

for i in folders_list:
    files_list = os.listdir(f'test/new/extracted_content/{i}')
    for k in files_list:
        with open(f'test/new/extracted_content/{i}/{k}', 'r', encoding='utf-8') as f:
            file_text = f.read()
            if re.search(pattern, file_text):
                print(f"{i}/{k}")
                print(re.search(pattern, file_text).group())
