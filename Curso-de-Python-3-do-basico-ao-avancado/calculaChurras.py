def calcular_rateio_completo(valor_total, pessoas):
    """
    Calcula o novo rateio do chope considerando as contribuições individuais.

    :param valor_total: Valor total do chope (ex: 590.00)
    :param pessoas: Dicionário com nomes como chaves e contribuições como valores
    :return: Saldo restante, lista de pessoas que não contribuíram e novo valor por pessoa
    """
    # Soma das contribuições
    total_contribuido = sum(pessoas.values())

    # Saldo restante
    saldo_restante = valor_total - total_contribuido

    # Pessoas que não contribuíram (valor = 0)
    pessoas_nao_contribuintes = [nome for nome, valor in pessoas.items() if valor == 0]

    # Novo rateio
    if len(pessoas_nao_contribuintes) > 0:
        novo_rateio = saldo_restante / len(pessoas_nao_contribuintes)
    else:
        novo_rateio = 0  # Todos já contribuíram

    return saldo_restante, pessoas_nao_contribuintes, novo_rateio


# --- Configuração ---
valor_total = 590.00
pessoas = {
    "Capí": 60.00,
    "Farny": 110.00,
    "Franklin": 100.00,
    "Wesley": 60.00,
    "Jhow": 60.00,
    "Dito": 60.00,
    "Tio Fá": 80.00,
    "Romildo": 60.00,  # Não contribuiu ainda
}

# --- Cálculo ---
saldo, nao_contribuintes, rateio_por_pessoa = calcular_rateio_completo(valor_total, pessoas)

# --- Resultado ---
print(f"Saldo restante: R$ {saldo:.2f}")
print(f"Pessoas que ainda não contribuíram: {nao_contribuintes}")
print(f"Novo rateio por pessoa: R$ {rateio_por_pessoa:.2f}" if rateio_por_pessoa > 0 else "Todos já contribuíram!")

