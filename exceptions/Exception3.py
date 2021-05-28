import sys

valor = input('Digite um numero')



try:
    numero = int(valor)
    print("bloco try")
    if(numero == 0):
     raise ValueError("Numero invalido")
except ValueError as error1:
    print('nao foi possivel converter, entre um digito valido', error1)
except Exception as err:
    print('aconteceu um erro inesperado: ')
else:
    print('na0 ocorreu nenhum erro')
finally:
    print('print finally')





