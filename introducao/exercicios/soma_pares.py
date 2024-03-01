def soma_numeros_pares(inicio, fim):
    if inicio > fim:
        print("O número inicial deve ser menor ou igual ao número final.")
        return
    
    soma = 0
    for i in range(inicio, fim + 1):
        if i / 2 == 0:
            soma += i  
    
    print("A soma dos números pares no intervalo [" + str(inicio) + ", " + str(fim) + "] eh: " + str(soma) )


soma_numeros_pares(1, 10)
