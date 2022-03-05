#!/usr/bin/python3


import fitz

#pdf_document = "Exams/OnlyText_2_pages.pdf"
pdf_document = 'Exams/ImagesAndText.pdf'

doc = fitz.open(pdf_document)
print ("number of pages: %i" % doc.pageCount)
print(doc.metadata)
print(doc.pageCount)

print("Primeiro for")
currentQuestion = 10
lastQuestion = 19

#Percorre todas as páginas do pdf
for i in range(0, doc.pageCount):

    #Extrai imagens da página atual
    for image in doc.getPageImageList(i):
        xref = image[0]
        pix = fitz.Pixmap(doc, xref)
        pix1 = fitz.Pixmap(fitz.csRGB, pix)
        pix1.writePNG("Images/page%s-%s.png" % (i, xref))
        pix1 = None
        pix = None

        print(doc.getPageImageList(i))
    #Fim das imagens

    page = doc.load_page(i)
    #Passa o conteúdo da página para uma String
    pageToString = page.get_text("text")

    print("segundo for")
    #Separar cada questão
    for j in range (currentQuestion, lastQuestion):
        question = "Questão " + str(j)
        print("QUESTAO --------------------" )
        print(question)
        if question in pageToString:
            index1 = pageToString.find(question)
            print(index1)
        else:
            print("Mudei de página")
            break

        nxtQuestion = "Questão " + str(j+1)
        if nxtQuestion in pageToString:
            index2 = pageToString.find(nxtQuestion)
            print(index2)
        else:
            index2 = len(pageToString)
            print(index2)


        print("3 for")
        #Extrair questão para um txt específico
        extracted = ""
        for k in range (index1, index2):
            extracted = extracted + pageToString[k]

        print("oi")
        print(extracted)
        f = open("Questions/" + str(j) + ".txt", "w")
        f.write(extracted)
        f.close()

        #Muda para próxima questão
        currentQuestion += 1
        print(currentQuestion)


#pageToString is String -> Find "Questão " in String
#If it founds question 10, so it writes on question 10

#Ver a leitura do gabarito
