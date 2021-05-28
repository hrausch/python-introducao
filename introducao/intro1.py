
def somar(a, b):
    c = a + b
    print('A soma eh: ', c)

def imprimir():
    print('funcao que imprime algo aleatorio')
# print
# print('Hello world')


# variavel1 = 'HERBERT'
# print('Meu nome eh: ' + variavel1)

#em python as variaveis sao dinamicamente tipadas:
# variavel1 = 23

# a linha abaixo ira gerar um erro: ao inves de concatenar ele tentara somar variavel1 com 
# a string.
# print("Minha idade eh:" + variavel1)

# a gente pode converter o inteiro para a string
# print('Minha idade eh: ' + str(variavel1))




# num1 = input('Qual a sua idade? ')
# string1 = 'O valor digitado foi: ' + num1 + ' !!'
# print(string1)

#note que num1 eh do tipo string, podemos converter para um inteiro
# num1 = int(num1)

# pq o print abaixo nao funciona?
# string2 = '\n ahaha'
# print("O valor digitado foi: ", num1, ' \n !!! uhu', string2 ,'Valeu!' ) 

# if( (num1 % 2) == 0):
#     print('Numero par')
#     print('hehe')
# else:
#     print('Numero impar')
#     print('uhu')


#loop com while
# tam = 5
# i = 0
# while( i < tam ):
#     print(i, ' ', end='')
#     i +=  1
# print('\n fim do while')



#loop com for
# tam = 10
# for i in range(0, tam):
#     print(i, ' ', end='')
# print('\n fim do for')

#no loop abaixo, i eh incrementado de 2 em 2
# for i in range(0, 10, 2):
#     print(i, ' ', end='')
#     if i > 5:
#         break
# print('\n fim do for')



#lista
# lista1 = [1, 2, 3]

# print('elemento no indice 1: ', lista1[1])

# lista1.append(23) #[1,2,3,23]
# lista1.append(14) # [1,2,3,23,14]
# lista1.append(3) # [1,2,3,23,14,3]
# print(lista1)
# lista1.sort() #ordenacao
# print(lista1)

# lista2 = []
# while(True):
#     numero = int(input('Digite o numero: '))
#     if(numero == 0):
#         break
#     else:
#         lista2.append(numero)

# print(lista2)
# lista2.sort()
# print(lista2)
# tamanho = len(lista2) #pega o numero de elemento / tamanho do vetor
# print('Tamanho da lista', tamanho)

# for(int i =0 ; i <= tamanho; i++){
#     elemento = lista[i]
#     print(elemento,' ', end='')
# }

# for i in lista2:
#     print(i,' ', end='')
# print('\n Fim do for')

# i = 0
# while(i < len(lista2)):
#     print(lista2[i], ' ', end='')
#     i += 1

# print('\n Fim do while')



somar(12,2)
somar(123,34)

