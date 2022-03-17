#!/usr/bin/python3

import fitz

#PDF path and name
pdf_document = 'Exams/gabarito2019.pdf'

#Extract data from pdf
doc = fitz.open(pdf_document)
page = doc.load_page(0)
pageToString = page.get_text("text")

#Write data on List
pageToList = pageToString.split("\n")
print(pageToList)

#Reference for english and spanish Answers
counter = 0
#Current question
number = 0

#Save each answer in which .txt
for i in range(0, len(pageToList)):

    element = pageToList[i].strip(" ")
    print("element " + element)

    if element.isnumeric():
        number = int(eval(str(element)))
        counter = 0

    elif len(element) == 1:

        counter += 1
        if number <= 5:
            if counter == 1:
                print("ENG")
                print(element)
                answer = open("Answers/" + str(number) + "-ENG.txt", "w")
            else:
                print("SPA")
                print(element)
                answer = open("Answers/" + str(number) + "-SPA.txt", "w")

        elif number > 0:
            answer = open("Answers/" + str(number) + ".txt", "w")

        answer.write(element)
        answer.close()
