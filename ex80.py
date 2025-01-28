# Inicializa uma lista vazia para armazenar os números inseridos
d = []

# Loop que se repete 5 vezes para receber 5 números do usuário
for i in range(5):
    # Solicita que o usuário digite um número
    n = int(input("dgt numero: "))
    
    # Se for o primeiro número, ele é adicionado diretamente à lista
    if i == 0:
        d.append(n)
    # Se o número digitado for maior que o último número da lista, adiciona no final
    elif n > d[-1]:
        d.append(n)
    else:
        # Se o número não for maior que o último, ele será inserido na posição correta
        pos = 0  # Inicia a posição em 0
        while pos < len(d):
            # Encontra a posição onde o número atual deve ser inserido
            if n <= d[pos]:
                d.insert(pos, n)  # Insere o número na posição correta
                break  # Sai do loop, pois a posição foi encontrada
            pos += 1  # Move para a próxima posição

# Exibe a lista ordenada ao final
print(d)
