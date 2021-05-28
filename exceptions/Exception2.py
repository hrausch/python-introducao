import sys

def func1():
    valor = int(input('Digite um numero'))

    if(valor == 0):
        print("zero")
        raise IndexError('Numero não pode ser zero')

    print(valor)
    
func1()




