#!/usr/bin/python3

import fitz

#pdf_document = fitz.open("ImagesAndText.pdf")
pdf_document = fitz.open("ImagesAndText.pdf")

for current_page in range(len(pdf_document)):
    for image in pdf_document.getPageImageList(current_page):
        xref = image[0]
        pix = fitz.Pixmap(pdf_document, xref)
        if pix.n < 5:        # this is GRAY or RGB
            pix.writePNG("Images/page%s-%s.png" % (current_page, xref))
        else:                # CMYK: convert to RGB first
            pix1 = fitz.Pixmap(fitz.csRGB, pix)
            pix1.writePNG("Images/page%s-%s.png" % (current_page, xref))
            pix1 = None
        pix = None

        print(pdf_document.getPageImageList(current_page))

#Tentar descobrir a localização da imagem na página
