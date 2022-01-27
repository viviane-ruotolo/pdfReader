#!/usr/bin/python3


myString = "Questão 10\nDisponível em: www.essl.pt. Acesso em: 9 maio 2019 (adaptado).\nEssa campanha se destaca pela maneira como utiliza a linguagem para conscientizar a sociedade da necessidade\nde se acabar com o bullying. Tal estratégia está centrada no(a)\nA chamamento de diferentes atores sociais pelo uso recorrente de estruturas injuntivas.\nB variedade linguística caracterizadora do português europeu.\nC restrição a um grupo específico de vítimas ao apresentar marcas gráficas de\nidentificação de gênero como “o(a)”.\nD combinação do significado de palavras escritas em línguas inglesa e portuguesa.\nE enunciado de cunho esperançoso “passe à história” no título do cartaz.\nQuestão 11\nEsporte e cultura: análise acerca da esportivização de práticas corporais nos jogos indígenas"


my_list = list(myString)
indices = [i for i, x in enumerate(my_list) if x == "Q"]
print(indices)

if "Questão 10" in myString:
    index10 = myString.find("Questão 10")
print(index10)
if "Questão 11" in myString:
    index11 = myString.find("Questão 11")
print(index11)

newString = ""
for i in range (index10, index11):
    newString = newString + myString[i]

print(newString)
