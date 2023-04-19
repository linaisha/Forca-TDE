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
    
    chances = 6

    oculta = [x for x in palavra]
    
    print(oculta)

    adivinhando = ""
    # começamos de fato o codigo
    while adivinhando != palavra or chances <= 0:
        # usuario digita uma letra
        letra = str(input("Digite uma letra: "))
        # não queremos que o usuario digite mais de uma letra
        if len(letra) > 1:
            print("Apenas UMA letra, seu vacilao!")
            #continue
        # incluir a letra digitada na lista
        digitadas.append(letra)
        # variavel da palavra que a pessoa esta adibinhando
        adivinhando = ""
        # aqui colocamos que se a pessoa acertar alguma letra, a mesma vai aparecer, senão ela mantem um _ no lugar
        for letrasegredo in palavra:
            if letrasegredo in digitadas:
                adivinhando += letrasegredo
            else:
                adivinhando += "_"
        # se errar a letra as chances diminuem em um
        if letra not in palavra:
            chances -= 1
            print("Você errou uma letra parceiro, que pena... -1 vida")

        # se as chances acabarem o jogo acaba com derrota
        if chances == 0:
            print("Vish, perdeu meu amigo! Foi enforcado!")
            V = 0

            break
        # dizemos quantas chances ainda restam
        # caso a pessoa conclua ela termina o jogo, caso não, a palavra aparece para ela ver o que falta
        print("Você possui ", chances, " chances, continue tentando!")
        if adivinhando != palavra:
            print("Palavra em andamento: ", adivinhando)
        else:
            print("Boa! Você conseguiu! A palavra secreta era: ", palavra)
            print('Parabens você ganhou')
            #break
            V = 1

    if V == 1 or V == 0:
        op = int(input('Você deseja continuar jogando? \n\n1 - Sim \n2 - Não \n'))
    
    if op == 2:
        break
    
# colocar o turle (desenho criado esta no arquivo auxiliar.py)
