"""
O programa deve ter um banco de lista de palavras predefinidas para serem utilizadas no jogo (utilizar biblioteca pickle).

Considere 3 níveis de dificuldade:

Fácil: Palavras de 4 a 5 letras

Médio: Palavras de 6 a 10 letras

Difícil: Palavras maiores que 10 letras ou “Frases Conhecidas”

O programa deve escolher uma palavra aleatoriamente.

O número de tentativas permitidas para o usuário deve ser proporcional ao tamanho da palavra. Por exemplo, se a palavra escolhida tiver 5 letras, o usuário deve ter 5 tentativas para acertar todas as letras.

O usuário deve poder inserir letras para tentar adivinhar a palavra.

O programa deve informar se a letra inserida pelo usuário está presente na palavra escolhida.

O programa deve mostrar a palavra em construção, com as letras adivinhadas até o momento e os espaços em branco (‘_’) para as letras não adivinhadas.

O programa deve informar ao usuário quando ele acertar a palavra ou quando acabarem suas tentativas.

O programa deve permitir que o usuário jogue novamente ou saia do jogo após a conclusão de uma partida.

O programa deve estar bem documentado e seguir as melhores práticas de programação.

#Ponto Extra#:

Aqueles que desejarem utilizar a biblioteca Turtle para desenhar a forca, podem receber até 2 pontos extras.

Neste caso, considere desenhar um corpo em formato palito, como o desenho abaixo. Considere 6 membros (Cabeça, Corpo, 2 braços e 2 pernas)

Alunos:
Elisa de Oliveira Martins, Maycon Ruani Nubesniak e João Henrique Ferreira Krüger
"""
# palavra exemplo so pra testar o codigo
palavra = "coelho"

# lista que guardará letras digitadas
digitadas = []

# aqui definimos quantas chances o jogador tem, como especificado no trabalho, a quantia ded chances sera a quantia de letras que a palavra tem
chances = len(palavra)

# fazendo a introdução do jogo
print("_"*114, "\n", "*"*38, " Bem vindo ao jogo da forca ", "*"*38)
print("Jogo desenvolvido por: Elisa de Oliveira Martins, Maycon Ruani Nubesniak e João Henrique Ferreira Krüger\n", "_"*114)

# opção se a pessoa quer de fato jogar
op = int(input("Deseja jogar?\n1. Sim\n2. Não\n"))
while op == 1:
    adivinhando = ""
    # começamos de fato o codigo
    while adivinhando != palavra or chances <= 0:

        # usuario digita uma letra
        letra = str(input("Digite uma letra: "))

        # não queremos que o usuario digite mais de uma letra
        if len(letra) > 1:
            print("Apenas UMA letra, seu vacilao!")
            continue
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

        # caso a pessoa conclua ela termina o jogo, caso não, a palavra aparece para ela ver o que falta
        if adivinhando == palavra:
            print("Boa! Você conseguiu! A palavra secreta era: ", palavra)
            break
        else:
            print("Palavra em andamento: ", adivinhando)

        # se errar a letra as chances diminuem em um
        if letra not in palavra:
            chances -= 1
            print("Você errou uma letra parceiro, que pena... -1 vida")

        # se as chances acabarem o jogo acaba com derrota
        if chances <= 0:
            print("Vish, perdeu meu amigo! Foi enforcado!")
            break

        # dizemos quantas chances ainda restam
        print("Você possui ", chances, " chances, continue tentando!")

# ele recomeça errado ja dando a vitoria, ver isso ai
# colocar o arquivo com pickle
# colocar dificuldades
# colocar aleatoriedade nas palavras (ver sugestao no arquivo tentativa pickle)
# colocar opção de recomeçar (da forma correta) e de sair do jogo
# ja fui documentando com os comentarios pra facilitar
# colocar o turle (desenho criado esta no arquivo auxiliar.py)
