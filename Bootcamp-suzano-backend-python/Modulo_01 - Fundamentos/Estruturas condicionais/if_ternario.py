# IF TERNÁRIO
#   Permite escrever uma condição em uma única linha.
#   É composto por três partes
#     1. Retorno caso a expressão retorne verdadeira
#     2. É a expressão lógica
#     3. É o retorno caso a expressão não seja atendida.

saldo = 200
saque = 500

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")