#!/usr/bin/python3


import fitz

#pdf_document = "OnlyText_2_pages.pdf"
#pdf_document = 'ImagesAndText.pdf'
pdf_document = 'ImagesAndText.pdf'

doc = fitz.open(pdf_document)
print ("number of pages: %i" % doc.pageCount)
print(doc.metadata)
print(doc.pageCount)


for i in range(0, doc.pageCount):
    page = doc.load_page(i)
    page1text = page.get_text("text")

    for j in range (10, 19):
        question = "Questão " + str(j)
        if question in page1text:
            index1 = page1text.find(question)
            print(index1)
        nxtQuestion = "Questão " + str(j+1)
        if nxtQuestion in page1text:
            index2 = page1text.find(nxtQuestion)
            print(index2)

        extracted = ""
        for k in range (index1, index2):
            extracted = extracted + page1text[k]

        print("oi")
        print(extracted)
        f = open("Questions/" + str(j) + ".txt", "w")
        f.write(extracted)
        f.close()


#page1text is String -> Find "Questão " in String
#If it founds question 10, so it writes on question 10
