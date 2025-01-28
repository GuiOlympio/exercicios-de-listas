# Inicializa uma lista vazia para armazenar os números inseridos
d = []

# Variável para contar quantos números já foram inseridos
cont = 0

# Laço para repetir 5 vezes (vai de 0 a 4)
for i in range(5):
    # Solicita ao usuário que digite um número e o armazena na variável 'n'
    n = int(input(f"dgt um numero para a posição {i}: "))
    
    # Adiciona o número digitado à lista 'd'
    d.append(n)
    
    # Incrementa o contador, que será usado para identificar o primeiro número
    cont += 1
    
    # Se for o primeiro número digitado, inicializa 'maior' e 'menor' com ele
    if cont == 1:
        maior = menor = d[i]
    else:
        # Se o número atual for maior que o maior número registrado, atualiza 'maior'
        if n > maior:
            maior = n
        # Se o número atual for menor que o menor número registrado, atualiza 'menor'
        elif n < menor:
            menor = n

# Exibe a lista completa de números digitados
print(d)

# Mostra o maior número encontrado e sua posição na lista
print(f'o maior {maior} na posição {d.index(maior)} ')

# Mostra o menor número encontrado e sua posição na lista
print(f'o menor {menor} na posição {d.index(menor)}')
