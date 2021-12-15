#!/usr/bin/python3

import fitz

pdf_document = "OnlyText_2_pages.pdf"
doc = fitz.open(pdf_document)
f = open("ReadingMuPDF.txt", "w")
print ("number of pages: %i" % doc.pageCount)
print(doc.metadata)
print(doc.pageCount)


for i in range(0, doc.pageCount):
    page = doc.loadPage(i)
    page1text = page.getText("text")
    f.write(page1text)


f.close()
