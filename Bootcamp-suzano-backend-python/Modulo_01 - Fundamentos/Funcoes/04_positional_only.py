# PARÂMETRO POR POSIÇÃO
# tudo que estiver antes da "/" é obrigatório ser somente por posição.

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    # Salvar carro no banco de dados...
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # inválido
