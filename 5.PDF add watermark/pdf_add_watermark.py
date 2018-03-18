#coding:utf-8

from PyPDF2 import PdfFileReader,PdfFileWriter

pdfFile = open('git-cheatsheet.pdf','rb')
pdfReader = PdfFileReader(pdfFile)
firstPage = pdfReader.getPage(0)

markFile = open('watermark.pdf','rb')
pdfWatermarkReader = PdfFileReader(markFile)

firstPage.mergePage(pdfWatermarkReader.getPage(0))

pdfWriter = PdfFileWriter()
pdfWriter.addPage(firstPage)

for pageNum in range(1,pdfReader.numPages):
    pageobj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageobj)

resultFile = open('add_watermark.pdf','wb')
pdfWriter.write(resultFile)

pdfFile.close()
markFile.close()
resultFile.close()