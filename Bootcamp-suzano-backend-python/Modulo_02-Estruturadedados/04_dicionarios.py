'''  DICIONÁRIO 
É declarado por chaves"{}" ou "dict"

'''
# Exemplos de declaração de dicionário

# Declarado por chaves
pessoa = {"nome": "Andreson", "idade": 50}

# Declarado por dict
pessoa = dict(nome="Andreson", idade=50)

# Adicionando uma nova chave no dicionário
pessoa["telefone"] = "3333-3333" # agora fica assim: {"nome": "Andreson", "idade": 50, "telefone": "3333-3333"}

# Acessando o dicionário
dados = {"nome": "Andreson", "idade": 50, "telefone": "3333-3333"}
dados["nome"]
dados["idade"]
dados["telefone"]

# alterando as informações no dicionário
dados["nome"] = "Maria"
dados["idade"] = 20
dados["telefone"] = "9999-9999"

# DICIONÁRIOS ANINHADOS - uma estrutura dentro da outra
contatos = {
    "andreson@gmail.com": {"nome": "Andreson", "telefone": "3333-3333"},
    "capi@gmail.com": {"nome": "Capi", "telefone": "9999-9999"},
    "andresoncapi@gmail.com": {"nome": "AndresonCapi", "telefone": "8888-8888"},
}

# Buscando o número do telefone do contato Capi
contatos["capi@gmail.com"]["telefone"] # Resposta: 9999-9999