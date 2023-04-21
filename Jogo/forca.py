# importando as bibliotecas
import pickle
import random
import turtle

def forca():
    turtle.left(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
def cabeca():
    turtle.circle(40)
def corpo():
    turtle.left(90)
    turtle.forward(200)
def perna_direita():
    turtle.left(45)
    turtle.forward(90)
def perna_esquerda():
    turtle.left(180)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(90)
def braco_direito():
    turtle.left(180)
    turtle.forward(90)
    turtle.left(45)
    turtle.forward(125)
    turtle.right(125)
    turtle.forward(90)
def braco_esquerdo():
    turtle.right(180)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(90)

# criação do arquivo pickle para chamar depois
"""
facil = ["bola","para","casa","fera","mira","goma","faca"]
medio = ["idade","igreja","sextou","saudade","serpente","nostalgia","algoritimos"]
dificil = ["paralelepipedo","desenvolvimento","otorrinolaringologista","desproporcionadamente","contrarrevolucionario","newtoniano","onomatopeia"]

filehandler1 = open("facil.pkl", "wb")
filehandler2 = open("medio.pkl", "wb")
filehandler3 = open("dificil.pkl", "wb")

pickle.dump(facil, filehandler1)
pickle.dump(medio, filehandler2)
pickle.dump(dificil, filehandler3)

filehandler1.close()
filehandler2.close()
filehandler3.close()
"""

# chama os arquivos criados
file1 = open("facil.pkl", "rb")
file2 = open("medio.pkl", "rb")
file3 = open("dificil.pkl", "rb")

facilt = pickle.load(file1)
mediot = pickle.load(file2)
dificilt = pickle.load(file3)

# lista que guardará letras digitadas
digitadas = []

# fazendo a introdução do jogo
print("_"*114, "\n", "*"*38, " Bem vindo ao jogo da forca ", "*"*38)
print("Jogo desenvolvido por: Elisa de Oliveira Martins, Maycon Ruani Nubesniak e João Henrique Ferreira Krüger\n", "_"*114)

# opção se a pessoa quer de fato jogar
op = int(input("Deseja jogar?\n1. Sim\n2. Não\n"))
while op == 1:
    # escolhendo entre as 7 palavras de cada dificuldade aleatoriamente
    aleatorio = random.randint(0, 6)

    # Escolhendo a dificuldade
    dif = int(input('Digite a dificuldade na qual você quer jogar \n\n1 - Facil \n2 - Medio \n3 - Dificil \n'))

    if dif == 1:
        palavra = (facilt[aleatorio])
    elif dif == 2:
        palavra = (mediot[aleatorio])
    elif dif == 3:
        palavra = (dificilt[aleatorio])
    else:
        print('erro')
    
    # este sera o segredo
    oculta = [x for x in palavra]

    # puxando o tamanho da palavra
    tam = len(oculta)

    P = 0

    adivinhando = []

    while(P < tam):
        adivinhando.append('-')
        P += 1

# aqui definimos quantas chances o jogador tem, como especificado no trabalho, a quantia ded chances sera a quantia de letras que a palavra tem
    chances = 6

    while chances > 0:
        letra = str(input('Digite uma letra:'))
        
        P = 0
        Flag = 0
        while P < tam:

            if oculta[P] == letra:
                adivinhando[P] = letra
                Flag = 1
            P += 1

        if Flag == 0:
            print(f'A letra {letra} não existe nessa palavra')
            chances -= 1



        if adivinhando == oculta:
            print('Você ganhou')
            break
            
        print(adivinhando)
        print(f'Você tem {chances} vidas')

        if chances == 6:
            turtle.clearscreen()
            turtle.setheading(0)
            forca()

        elif chances == 5:
            turtle.clearscreen()
            turtle.setheading(0)
            forca()
            cabeca()

        elif chances == 4:
            turtle.clearscreen()
            turtle.setheading(0)
            forca()
            cabeca()
            corpo()

        elif chances == 3:
            turtle.clearscreen()
            turtle.setheading(0)
            forca()
            cabeca()
            corpo()
            perna_direita()

        elif chances == 2:
            turtle.clearscreen()
            turtle.setheading(0)
            forca()
            cabeca()
            corpo()
            perna_direita()
            perna_esquerda()

        elif chances == 1:
            turtle.clearscreen()
            turtle.setheading(0)
            forca()
            cabeca()
            corpo()
            perna_direita()
            perna_esquerda()
            braco_direito()

        elif chances == 0:
            turtle.clearscreen()
            turtle.setheading(0)
            forca()
            cabeca()
            corpo()
            perna_direita()
            perna_esquerda()
            braco_direito()
            braco_esquerdo()
    
    if chances == 0:
        print('Você perdeu todas as suas vidas')

    op = int(input('Você deseja continuar jogando? \n\n1 - para continuar \n2 - para parar \n'))

print('Obrigado por jogar')
