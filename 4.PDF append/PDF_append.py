#coding:utf-8

import PyPDF2

filenames = ['git-cheatsheet_部分1.pdf','git-cheatsheet_部分2.pdf']

merger = PyPDF2.PdfFileMerger()

for filename in filenames:
    merger.append(PyPDF2.PdfFileReader(filename))

merger.write('git-cheatsheet.pdf')