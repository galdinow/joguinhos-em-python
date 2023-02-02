from random import choice
from random import randint


def jogar():
    # cabecalho do jogo
    abertura_jogo()

    # Criando variaveis
    erros = 0
    acerto = False

    # Sorteio do tema
    escolha_tema = randint(1, 3)
    if escolha_tema == 1:
        tema = 'frutas'
        banco_de_palavras = open('frutas', 'r')
    elif escolha_tema == 2:
        tema = 'paises'
        banco_de_palavras = open('paises', 'r')
    else:
        tema = 'partes do corpo humano'
        banco_de_palavras = open('pdc', 'r')

    # Sorteio da palavra secreta
    lista_de_palavras = []
    for palavra in banco_de_palavras:
        lista_de_palavras.append(palavra.strip())

    palavra_secreta = choice(lista_de_palavras).lower()

    # Fechando o arquivo usado
    banco_de_palavras.close()

    # Criando a forca
    forca = []
    for letra in palavra_secreta:
        forca.append('_')
    print(forca)

    # Codigo do jogo em si
    while not acerto and not erros == 10:
        chute = str(input('Qual letra vc quer tentar? ')).lower().strip()

        # Checando o chute e calculando os erros
        if chute in palavra_secreta:
            for c, v in enumerate(palavra_secreta):
                if chute == v:
                    forca[c] = chute
        else:
            erros += 1
        print(f'Voce ja errou {erros} vezes!')
        print(forca)

        # Dica
        if erros == 5:
            print(f'Aqui vai uma dica: o tema eh {tema}')

        # Condicao de vitoria
        acerto = '_' not in forca

        # Mensagens de vitoria/derrota
        if erros == 10 and not acerto:
            print('Voce perdeu! RUIM!!!')
            print(f'A palavra secreta era {palavra_secreta}')
        elif acerto:
            print('QUE CARA BOM PQP!!! BOOOA')


# Funcoes para simplificar o codigo
def abertura_jogo():
    print('--------------------------------')
    print('Seja bem-vinde ao jogo da Forca!')
    print('--------------------------------')
    print('Tente acertar a palavra errando menos de 10 vezes! ')
    print()


# Roda o arquivo diretamente e nao pelo menu criado
if __name__ == '__main__':
    jogar()
