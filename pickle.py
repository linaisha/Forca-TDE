# importando o pickle
import pickle
"""
facil = ["bola","para","casa","fera","mira","goma","faca"]
medio = ["idade","igreja","sextou","saudade","serpente","nostalgia","algoritimos"]
dificil = ["paralelepipedo","desenvolvimento","otorrinolaringologista","desproporcionadamente","contrarrevolucionario","newtoniano","onomatopeia"]

arq1 = open("facil.pkl","wb")
arq2 = open("medio.pkl","wb")
arq3 = open("dificil.pkl","wb")

pickle.dump(facil, arq1)
pickle.dump(medio, arq2)
pickle.dump(dificil, arq3)
"""


arq1 = open("facil.pkl","rb")
arq2 = open("medio.pkl","rb")
arq3 = open("dificil.pkl","rb")

teste = pickle.load(arq1)
print(teste[0])


