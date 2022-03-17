#!/usr/bin/python3


import fitz

#pdf_document = "OnlyText_2_pages.pdf"
#pdf_document = 'ImagesAndText.pdf'
pdf_document = 'Exams/gabarito2020.pdf'
#pdf_document = 'Exams/gabarito2019.pdf'

doc = fitz.open(pdf_document)
f = open("Answers2020.txt", "w")
#f = open("Answers.txt", "w")
print ("number of pages: %i" % doc.pageCount)
print(doc.metadata)
print(doc.pageCount)


page = doc.load_page(0)
pageToString = page.get_text("text")
f.write(pageToString)

pageToList = pageToString.split("\n")
print(pageToList)

number = 0
for i in range(0, len(pageToList)):
    try:
        temp = int(eval(str(pageToList[i])))
        if type(temp) == int:
            number = temp
            #se for número eu atualizo o number
            #fazer as condicionais pra ing e esp
    except:
        temp = int(eval(str(pageToList[i])))
        answer = open("Answers/" + str(number) + ".txt", "w")
        answer.write(temp)
        answer.close()
        #se não for, eu salvo no último number
    print(number)




#ListToInt = int(pageToList[5])

#print(ListToInt)

#Talvez mudar o lugar disso aqui
f.close()
#page1text is String -> Find "Questão " in String
#If it founds question 10, so it writes on question 10
