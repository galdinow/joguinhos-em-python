from random import randint


def jogar():
    # cabecalho do jogo
    abertura_jogo()

    # Iniciando as variaveis
    numero_secreto = randint(1, 100)
    chute = 0
    pontos = 1000

    # Selecionando dificuldade
    print('Por favor selecione a sua dificuldade!')
    print('(1) Facil (2) Medio (3) Dificil')

    dificuldade = int(input('Digite aqui: '))

    # Checa se eh um valor valido
    while dificuldade > 3:
        print('Por favor, digite apenas valores validos!')
        dificuldade = int(input('Digite aqui: '))

    # Seleciona tentativas com base na dificuldade selecionada
    if dificuldade == 1:
        tentativas = 20
    elif dificuldade == 2:
        tentativas = 10
    else:
        tentativas = 5

    # Jogo em si
    print(f'Seu jogo comeca com {tentativas} tentativas!')
    while tentativas > 0 and chute != numero_secreto:
        chute = int(input('Digite um numero entre 1 e 100:'))

        # Checa se o chute eh valido
        if chute > 100 or chute < 1:
            while chute > 100 or chute < 1:
                chute = int(input('Por favor, escolha apenas numeros entre 1 e 100:'))
        # Checagem do chute
        if chute > numero_secreto:
            print('Tente chutar mais baixo.')
        elif chute < numero_secreto:
            print('Tente chutar mais alto.')

        # Calculo dos pontos
        pontos_perdidos = abs(numero_secreto - chute)
        pontos -= pontos_perdidos

        # Calculo das tentativas
        tentativas -= 1
        print(f'Voce ainda tem {tentativas} tentativas!')
        print('---------------------------------')

    # Mensagem de vitoria/derrota
    if chute == numero_secreto:
        print(f'parabens, voce acertou!!')
        print(f'e fez {pontos} pontos')
    else:
        print(f'Voce eh ruim! :/')
        print(f'o numero secreto era {numero_secreto}')


# Funcoes para simplificar o codigo
def abertura_jogo():
    print('---------------------------------')
    print('Bem-vinde ao jogo da adivinhacao!')
    print('---------------------------------')


# Roda o arquivo diretamente e nao pelo menu criado
if __name__ == '__main__':
    jogar()
