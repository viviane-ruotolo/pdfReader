#!/usr/bin/python3


import fitz

#pdf_document = "OnlyText_2_pages.pdf"
#pdf_document = 'ImagesAndText.pdf'
pdf_document = 'ImagesAndText.pdf'

doc = fitz.open(pdf_document)
f = open("ReadingMuPDF.txt", "w")
print ("number of pages: %i" % doc.pageCount)
print(doc.metadata)
print(doc.pageCount)


for i in range(0, doc.pageCount):
    page = doc.load_page(i)
    page1text = page.get_text("text")
    f.write(page1text)


f.close()
#page1text is String -> Find "Questão " in String
#If it founds question 10, so it writes on question 10
