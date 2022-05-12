import PyPDF2
import re

data = open('python_bootcamp/section_17_csv_pdf/Find_the_Phone_Number.pdf', 'rb')

pattern = r'\d{3}\S\d{3}\S\d{4}'
pdf_reader = PyPDF2.PdfFileReader(data)

for num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(num)
    text = page.extractText()
    real_text = text.replace(" ", "")
    match = re.search(pattern, real_text)
    if match:
        print(match.group())
