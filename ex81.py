# Inicializa uma lista vazia para armazenar os números
d = []

# Loop principal que continua até o usuário decidir parar
while True:
    # Solicita ao usuário que digite um número
    n = int(input("dgt um numero: "))
    
    # Verifica se o número ainda não está na lista
    if n not in d:
        d.append(n)  # Adiciona o número à lista se não for duplicado
    
    # Inicializa a variável de resposta para controle do fluxo
    resp = ' '
    # Garante que o usuário insira apenas 'S' ou 'N'
    while resp not in 'SN':
        resp = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    
    # Se o usuário digitar 'N', encerra o loop principal
    if resp == 'N':
        break

# Verifica se o número 5 está presente na lista
for i in d:
    if i == 5:
        print("numero 5 encontrado")

# Ordena a lista em ordem decrescente
d.sort(reverse=True)

# Exibe a lista final
print(d)
