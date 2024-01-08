'''
Neste script serao apresentados manipulacoes de listas/vetores em python


'''


# DEFINICAO DE LISTA
lista1 = [1, 2, 3]

# ACESSANDO POSICAO DA LISTA.
# o indexamento se inicia na posicao 0.
print('elemento no indice 1: ', lista1[1])

# ADICIONANDO ELEMENTO NO FINAL DA LISTA
# Funcao append.
lista1.append(23) #[1,2,3,23]
lista1.append(14) # [1,2,3,23,14]
lista1.append(3) # [1,2,3,23,14,3]
print(lista1)

# ORDENACAO DA LISTA
lista1.sort() #ordenacao
print(lista1)


lista2 = []
'''
No loop abaixo eh adicionado elemento na lista ate que le o numero 0
'''
while(True):
    numero = int(input('Digite o numero: '))
    if(numero == 0):
        break
    else:
        lista2.append(numero)
print(lista2)

# TAMANHO DO VETOR -> FUNCAO LEN
tamanho = len(lista2)
print('Tamanho da lista', tamanho)

'''
PERCORRENDO O VETOR.

O trecho de codigo abaixo eh uma maneira de percorrer o vetor escrito em c, ou java.

for(int i =0 ; i <= tamanho; i++){
     elemento = lista[i]
     print(elemento,' ', end='')
 }

 a seguir, formas de como fazer este loop em python
'''

# FORMA 1
for i in lista2:
    print(i,' ', end='')
print('\n Fim do for')

# FORMA 2
i = 0
while(i < len(lista2)):
    print(lista2[i], ' ', end='')
    i += 1
print('\n Fim do while')


# LIMPANDO VETOR
lista1[:] = []



'''
Manipulacao de String
'''

texto = "Python"
# imprime o caracter na posicao 0 = P
print(texto[0])

# imprime o caracter na posicao 6 = n
print(texto[5])
# pode-se usar indices negativos
print(texto[-1])

# intervalo
print(texto[0:2]) #indice 0 eh incluido e o 2 excluido
print(texto[:3])# do primeiro indica ate o indice 2
print(texto[3:])# do indice 3 ate o final


'''
MATERIAL P/ APROFUNDAMENTO:
https://docs.python.org/3/tutorial/introduction.html
'''