import pickle
import random

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

file1 = open("facil.pkl", "rb")
file2 = open("medio.pkl", "rb")
file3 = open("dificil.pkl", "rb")

facilt = pickle.load(file1)
mediot = pickle.load(file2)
dificilt = pickle.load(file3)

# lista que guardará letras digitadas
digitadas = []

# aqui definimos quantas chances o jogador tem, como especificado no trabalho, a quantia ded chances sera a quantia de letras que a palavra tem

# fazendo a introdução do jogo
print("_"*114, "\n", "*"*38, " Bem vindo ao jogo da forca ", "*"*38)
print("Jogo desenvolvido por: Elisa de Oliveira Martins, Maycon Ruani Nubesniak e João Henrique Ferreira Krüger\n", "_"*114)

# opção se a pessoa quer de fato jogar
op = int(input("Deseja jogar?\n1. Sim\n2. Não\n"))
while op == 1:
    aleatorio = random.randint(0, 6)

    dif = int(input('Digite a dificuldade na qual você quer jogar \n\n1 - Facil \n2 - Medio \n3 - Dificil \n'))

    if dif == 1:
        palavra = (facilt[aleatorio])
    elif dif == 2:
        palavra = (mediot[aleatorio])
    elif dif == 3:
        palavra = (dificilt[aleatorio])
    else:
        print('erro')
    
    oculta = [x for x in palavra]

    tam = len(oculta)
    
    print(oculta)

    P = 0

    adivinhando = []

    while(P < tam):
        adivinhando.append('-')
        P += 1

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
        print('Vocẽ perdeu todas as suas vidas')

    op = int(input('Você deseja continuar jogando? \n\n1 - para continuar \n2 - para parar \n'))

print('Obrigado por jogar')
