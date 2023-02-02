import forca
import adivinhacao

# Cabecalho do menu
print('--------------------------------------')
print('ESCOLHA SEU JOGO!')
print('--------------------------------------')
print('(1) Forca (2) Adivinhacao')

# Verificando se a escolha foi valida
jogo = int(input('Qual jogo? '))
while jogo > 2:
    print('Por favor, digite apenas os numeros indicados.')
    jogo = int(input('Digite novamente: '))

# Escolha do jogo
if jogo == 1:
    print('jogando jogo da Forca')
    forca.jogar()
elif jogo == 2:
    print('Jogando jogo da Adivinhacao')
    adivinhacao.jogar()
