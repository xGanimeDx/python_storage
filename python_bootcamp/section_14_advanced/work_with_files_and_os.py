import os
import shutil

f = open("python_bootcamp/section_14_advanced/test.txt", 'w+', encoding='utf-8')
f.write('test text')
f.close()

print(os.getcwd())
print(os.listdir())

shutil.move("python_bootcamp/section_14_advanced/test.txt", "python_bootcamp/")
