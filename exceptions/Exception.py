import sys

valor = input('Digite um numero')

try:
    numero = int(valor)
    # f = open('arquivo.txt')
except OSError as err:
    print('arquivo.txt nao existe. por favor, crie no diretorio')
except ValueError:
    print('nao foi possivel converter, entre um digito valido')
    # valor = input('Digite um numero')
    # numero = int(valor)
except:
    print('aconteceu um erro inesperado: ', error)
finally:
    print('bloco finally executado')



print('programa continuou a rodar')
print('programa continuou a rodar 1')
print('programa continuou a rodar 2')





# try:
#     f = open('arquivo.txt')

#     numero = int(valor)

# except OSError as err:
#     print('Erro de IO')
# except ValueError:
#     print('Nao eh possivel converter')
# except:
#     print('erro inesperado')
#     raise