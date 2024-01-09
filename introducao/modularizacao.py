'''
Neste script são apresentados exemplos de funcoes/procedimentos em Python
'''

def soma(a, b):
    '''
    Recebe dois parametros e retorna o valor da soma deles
    '''
    return a  + b

total = soma(10, 5)
print(total)


def divisao(a, b=1):
    '''
    Recebe dois parametros, sendo que ´b´ possui um valor default caso nao seja passado na chamada 
    da funcao.
    retorna a divisao de a e b
    '''
    return a/b

div1 = divisao(10)
div2 = divisao(12, 4)


def soma_divisao(a, b):
    '''
    Nesta funcao recebe dois parametros e retorna o valor da soma e divisao deles.
    '''
    soma = a + b
    divisao = a / b
    return soma, divisao

soma1, divisao1 = soma_divisao(12, 4)
print(soma1)
print(divisao1)

def value(x):
    '''
    Em Python a passagem de parametro eh feita por valor.
    '''
    x = 1

x = 0
value(x)
print(x)


'''
MATERIAL P/ APROFUNDAMENTO:

https://docs.python.org/3/tutorial/controlflow.html#defining-functions
'''