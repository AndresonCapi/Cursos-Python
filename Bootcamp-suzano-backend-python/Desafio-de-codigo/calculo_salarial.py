

def calcular_imposto(salario):
    aliquota = 0.00
    if (salario >= 0 and salario <= 1100):
        aliquota = 0.05
    elif (salario >= 1100.01 and salario <= 2500):
        aliquota = 0.10
    else :
        aliquota = 0.15
    return aliquota * salario

valor_salario = float(input())
valor_beneficio = float(input())

valor_imposto = calcular_imposto(valor_salario)
saida = valor_salario - valor_imposto + valor_beneficio
print(f'{saida:.2f}')




def calcular_saldo(transacoes):
    saldo = 0

    # TODO: Itere sobre cada transação na lista:
    for transacao in transacoes:
        # TODO: Adicione o valor da transação ao saldo
        saldo += transacao

    # TODO: Retorne o saldo formatado em moeda brasileira com duas casas decimais:
    return f"Saldo: R$ {saldo:.2f}"


entrada_usuario = input()

entrada_usuario = entrada_usuario.strip("[]").replace(" ", "")

transacoes = [float(valor) for valor in entrada_usuario.split(",")]

# TODO: Calcule o saldo com base nas transações informadas:
resultado = calcular_saldo(transacoes)

print(resultado)
