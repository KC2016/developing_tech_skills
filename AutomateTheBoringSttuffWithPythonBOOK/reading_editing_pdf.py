import PyPDF2
import os
os.getcwd()
os.chdir('/Tutorials')

# # read
# pdfFile = open('Resume.pdf', 'rb')   # read binary

# reader = PyPDF2.PdfFileReader(pdfFile)
# print(reader.numPages)
# page = reader.getPage(0)
# print(page.extractText())

# for pageNum in range(reader.numPages):
#     print(reader.getPage(pageNum).extractText())

# write
pdf1File = open('Resume.pdf', 'rb')
pdf2File = open('Resume copy.pdf', 'rb')  # read binary mode
reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)
writer = PyPDF2.PdfFileWriter() # new blank pdf

for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader2.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

outputFile = open('combineResume.pdf', 'wb')  # write binary mode
writer.write(outputFile)
outputFile.close()
pdf1File.close()
pdf1File.close()