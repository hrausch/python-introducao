def verificar_palindromo(palavra):

    
    # Verificando se a palavra é um palíndromo
    palindromo = True
    tamanho = int(len(palavra) / 2)
    for i in range(tamanho):
        if palavra[i] != palavra[-i]:
            palindromo = False
            break
    
    if palindromo:
        print("A palavra "+palavra+" é um palíndromo.")
    else:
        print("A palavra "+ palavra +" não é um palíndromo.")


verificar_palindromo("ararar")
