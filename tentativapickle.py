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
# importando o pickle
import pickle
import Segredos from arquivo


# class Segredos:
#     facil1 = "bola"
#     facil2 = "idade"
#     medio1 = "igreja"
#     medio2 = "sextou"
#     medio3 = "saudade"
#     medio4 = "serpente"
#     medio5 = "nostalgia"
#     medio6 = "algoritimos"
#     dificil1 = "paralelepipedo"
#     dificil2 = "desenvolvimento"


# palavras = open("arquivo.pkl", "wb")
# pickle.dump(Segredos, palavras)
if __name__ == "__main__":

    palavras = open("arquivo.pkl", "rb")
    teste = pickle.load(palavras)

    print(teste.facil1)
