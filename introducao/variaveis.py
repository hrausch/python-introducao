'''
Este eh o primeiro script python.

Aqui sera apresentado como funciona a declaracao de variavel na linguagem

1) Python nao requer tipo na definicao de variaveis
2) Nao ha o ; no final da sentenca


'''

# DEFINIÇÃO E ATRIBUICAO DE VARIAVEIS
altura = 10
largura = 5
area = altura * largura

# IMPRIMINDO VALOR DE VARIAVEL
print(altura)
print(largura)
print(altura, largura)

# DEFININDO STRING
# definindo string. utiliza-se ' ou " . O resultado eh o mesmo.
texto_chamada = 'A area do retangulo eh'
texto_chamada = "A area do retangulo eh"

print(texto_chamada)


# CONCATENANDO STRINGS
texto_resultado = texto_chamada + " (lado * altura) :"
print(texto_resultado)

'''
texto_resultado = texto_chamada + str(area)
- neste momento do codigo a variavel area contem um valor inteiro.
- assim, eh preciso 'converter' este valor inteiro para string.
- o metodo 'str' executa essa funcao
'''
texto_resultado_final = texto_resultado + str(area)
print(texto_resultado_final)

#ALTERANDO O TIPO DE VARIAVEL
print(type(area)) # 'type retorna o tipo de variavel
 
area = "novo valor para area"
print(type(area))

# neste momento eh preciso usar str para concatenar a variavel area com outra string?

'''
MATERIAL P/ APROFUNDAMENTO:
https://docs.python.org/3/tutorial/introduction.html
'''