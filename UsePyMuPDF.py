#!/usr/bin/python3

#Erro na linha 18 ????
import fitz

#pdf_document = "OnlyText_2_pages.pdf"
pdf_document = 'ImagesAndText.pdf'

doc = fitz.open(pdf_document)
f = open("ReadingMuPDF.txt", "w")
print ("number of pages: %i" % doc.pageCount)
print(doc.metadata)
print(doc.pageCount)


for current_page in range(0, doc.pageCount):
    page = doc.loadPage(current_page)
    page1text = page.getText("text")
    for image in pdf_document.getPageImageList(current_page):
        xref = image[0]
        pix = fitz.Pixmap(pdf_document, xref)
        if pix.n < 5:        # this is GRAY or RGB
            pix.writePNG("page%s-%s.png" % (current_page, xref))
        else:                # CMYK: convert to RGB first
            pix1 = fitz.Pixmap(fitz.csRGB, pix)
            pix1.writePNG("page%s-%s.png" % (current_page, xref))
            pix1 = None
        pix = None


    f.write(page1text)


f.close()
