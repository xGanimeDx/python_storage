import zipfile

f = open('python_bootcamp/section_14_advanced/fileone.txt', 'w+', encoding='utf-8')
f.write('one file')
f.close()

f = open('python_bootcamp/section_14_advanced/filetwo.txt', 'w+', encoding='utf-8')
f.write('two file')
f.close()

comp_file = zipfile.ZipFile('python_bootcamp/section_14_advanced/comp_file.zip', 'w')

comp_file.write('python_bootcamp/section_14_advanced/fileone.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('python_bootcamp/section_14_advanced/filetwo.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

zip_obj = zipfile.ZipFile('python_bootcamp/section_14_advanced/comp_file.zip', 'r')
zip_obj.extractall('python_bootcamp/section_14_advanced/extracted')