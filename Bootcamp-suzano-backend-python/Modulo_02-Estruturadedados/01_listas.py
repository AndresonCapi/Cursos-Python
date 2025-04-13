# LISTAS

# Exemplo de criação de listas utilizando colchetes "[]"
frutas = ["laranja", "maca", "uva"]
print(frutas)

frutas = []
print(frutas)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

# Exemplo de criação de listas utilizando a palavra reservada "list"
letras = list("Python") # cada letra é um elemento
print(letras)

numeros = list(range(10)) # Essa lista vai gerar valores de 0 a 9
print(numeros)

# Acessando os dados da lista
frutas = ["laranja", "maca", "uva"]
frutas[0] # laranda
frutas[1] # maca
frutas[2] # uva

# Índice negativo - contagem começa em -1, ou seja, começa pelo último item da lista
frutas = ["laranja", "maca", "uva"]
frutas[-1] # uva
frutas[-2] # maca

# Lista aninhadas, ou seja, lista que armazena outras listas. Matriz
# ... Com isso, podemos criar estruturas bidimensionais (tabelas), 
# ... e acessar informando os índices de LINHA e COLUNA.

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

matriz[0] # [1, "a", 2]
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # "c"

# Fatiamento - Passar um 
#posição  0    1    2    3    4    5
lista = ["p", "y", "t", "h", "o", "n"]

lista[2:]    # ["t", "h", "o", "n"] início posição 2 até o fim
lista[:2]    # ["p", "y"] - antes da posição 2
lista[1:3]   # ["y", "t"] início posição 1 até antes da posição 3 
lista[0:3:2] # ["p", "y", "t", "h", "o", "n"] início posição 0 até antes da posição 3, pulando a cada 2 casas
lista[::]    # ["p", "y", "t", "h", "o", "n"] passar toda a sequência
lista[::-1]  # ["p", "y", "t", "h", "o", "n"] inverter/espelhar uma sequência

# Iteração com a lista - Utilizando o FOR

carros = ["Gol", "Celta", "Palio"]

for carro in carros:
    print(carro)


numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)


# outro exemplo
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]