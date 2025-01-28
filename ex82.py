# Inicializa uma lista vazia para armazenar todos os números digitados
d = []

# Loop principal que continua até o usuário decidir parar
while True:
    # Solicita ao usuário que digite um número e adiciona à lista principal
    n = int(input("dgt um numero: "))
    d.append(n)
    
    # Controle de resposta para continuar ou parar
    resp = ' '
    # Garante que o usuário insira apenas 'S' ou 'N'
    while resp not in 'SN':
        resp = str(input("continuar [S/N]: ")).strip().upper()[0]
    
    # Sai do loop principal se o usuário digitar 'N'
    if resp == 'N':
        break

# Organiza a lista principal em ordem crescente
d.sort()

# Inicializa listas separadas para números pares e ímpares
par = []
impar = []

# Percorre a lista principal e separa os números em pares ou ímpares
for i in d:
    if i % 2 == 0:  # Verifica se o número é par
        par.append(i)  # Adiciona à lista de pares
    else:  # Caso contrário, é ímpar
        impar.append(i)  # Adiciona à lista de ímpares

# Exibe a lista completa, a de pares e a de ímpares
print(d)       # Lista principal ordenada
print(par)     # Lista com números pares
print(impar)   # Lista com números ímpares
