'''
Neste script serao apresentados as formas de condicional em python.

1) Os 'blocos' em pyhton sao definidos pela identacao, nao ha uso de {}


'''

# O comando 'input' eh uma forma de fazer leitura de dados pelo console
x = int(input("Digite um numero: "))

# verifica se o numero eh par.
if (x % 2) == 0:
    print('x eh par')

# if e else
if (x % 2) == 0:
    print('x eh par')
else:
    print('x eh impar')

# blocos com if e else
if (x > 10):
    print('x eh maior que 10')
    x = x / 10
    print(x)
else:
    print('x eh menor que 10')
    x = x * 10
    print(x)

# blocos com if, elseif, e else
if ( x > 100):
    print('x maior que 100')

    if (x % 2) == 0:
        print('x eh par')

elif ( x > 50):
    print('x maior que 50 e menor que 100')
else:
    print('x menor que 50')    


'''
MATERIAL P/ APROFUNDAMENTO:
https://docs.python.org/3/tutorial/introduction.html
'''