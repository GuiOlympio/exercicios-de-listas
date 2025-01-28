# Inicializa uma lista vazia para armazenar os números inseridos
l = []

# Início de um loop infinito, que será interrompido manualmente
while True:
    # Solicita ao usuário que digite um número inteiro
    n = int(input('dgt numero : '))

    # Verifica se o número já está na lista
    if n not in l:
        # Se não estiver, adiciona o número à lista
        l.append(n)
    else:
        # Se o número já estiver na lista, informa que ele é duplicado
        print("Valor duplicado")

    # Variável para controlar a resposta do usuário (deseja continuar?)
    resp = ' '  # Inicializada como um espaço vazio para entrar no próximo loop
    
    # Enquanto o usuário não responder com 'S' ou 'N', continua pedindo uma resposta válida
    while resp not in 'SN':
        resp = str(input('deseja continuar? [S/N]: ')).strip().upper()[0]
    
    # Se o usuário responder 'N', o loop principal é interrompido
    if resp == 'N':
        break

# Ordena os números na lista em ordem crescente
l.sort()

# Exibe a lista ordenada
print(l)
