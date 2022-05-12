import PyPDF2

f = open('python_bootcamp/section_17_csv_pdf/Working_Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
print(pdf_reader.numPages)

page_one = pdf_reader.getPage(0)
page_one_text = page_one.extractText()
print(page_one_text)
f.close()

f = open('python_bootcamp/section_17_csv_pdf/Working_Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)

first_page = pdf_reader.getPage(0)
pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(first_page)
pdf_output = open('python_bootcamp/section_17_csv_pdf/Some_BrandNew_Doc.pdf', 'wb')
pdf_writer.write(pdf_output)
f.close()
pdf_output.close()

f = open('python_bootcamp/section_17_csv_pdf/Working_Business_Proposal.pdf', 'rb')
pdf_text = []
pdf_reader = PyPDF2.PdfFileReader(f)
for num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(num)
    pdf_text.append(page.extractText())

print(pdf_text)
