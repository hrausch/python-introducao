'''
Neste script serao apresentados as formas de estrutura de repeticao no python


'''


#loop com for
tam = 10
for i in range(0, tam):
    print(i, ' ', end='')
    print('\n fim do for')

#no loop abaixo, i eh incrementado de 2 em 2
for i in range(0, 10, 2):
    print(i, ' ', end='')
    if i > 5:
        break
print('\n fim do for')


#loop com while
tam = 5
i = 0
while( i < tam ):
    print(i, ' ', end='')
    i +=  1
print('\n fim do while')

'''
MATERIAL P/ APROFUNDAMENTO:
https://docs.python.org/3/tutorial/introduction.html
'''