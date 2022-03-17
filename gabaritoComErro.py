#!/usr/bin/python3


import fitz

#pdf_document = "OnlyText_2_pages.pdf"
#pdf_document = 'ImagesAndText.pdf'
#pdf_document = 'Exams/gabarito2020.pdf'
pdf_document = 'Exams/gabarito2019.pdf'

doc = fitz.open(pdf_document)
#f = open("Answers2020.txt", "w")
f = open("Answers.txt", "w")
print ("number of pages: %i" % doc.pageCount)
print(doc.metadata)
print(doc.pageCount)


page = doc.load_page(0)
pageToString = page.get_text("text")

#Posso apagar esse txt depois
f.write(pageToString)
f.close()

pageToList = pageToString.split("\n")
print(pageToList)

counter = 0
number = 0
for i in range(0, len(pageToList)):

    element = pageToList[i].strip(" ")
    #print(element)
    if element.isnumeric():
        #testar se a sring tem só números e condições para salvar respostas
        #print("É um número")
        number = int(eval(str(element)))
        counter = 0

    elif len(element) == 1:

        if number <= 5:
            if counter <= 1:
                answer = open("Answers/" + str(number) + "-ENG.txt", "w")
                counter += 1
            else:
                #Salva as respostas do espanhol em inglês
                answer = open("Answers/" + str(number) + "-SPA.txt", "w")

        elif number > 0:
            answer = open("Answers/" + str(number) + ".txt", "w")

        answer.write(element)
        answer.close()
    #print(len(element))





#ListToInt = int(pageToList[5])

#print(ListToInt)

#page1text is String -> Find "Questão " in String
#If it founds question 10, so it writes on question 10
