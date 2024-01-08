'''
Neste script serao apresentados as formas de condicional em python. 'switch/case
Em python a palavra reservada eh o match, e nao case.
Nessa estrutura o valor de uma expressao eh comparada com sucessivos padroes em um ou mais bloco case
'''

# importando biblioteca random gera numero aleatorio
import random

#o limite inferior do intervalo eh incluido, mas o superior nao.
x = random.randrange(1, 10)

match x:
    case 2:
        print('x eh par')
    case 3:
        print('x eh o primo 3')

print('****')

# case _  -> qualquer outro caso nao satisfeito eh abordado nesse bloco.
match x:
    case 2:
        print('x eh par')
    case 3:
        print('x eh o primo 3')
    case _:
        print('outros numeros')
        print(x)


'''
MATERIAL P/ APROFUNDAMENTO:
https://docs.python.org/3/tutorial/introduction.html
'''