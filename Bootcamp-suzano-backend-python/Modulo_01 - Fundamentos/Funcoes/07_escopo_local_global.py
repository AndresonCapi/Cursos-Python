# ESCOPO LOCAL é tudo que está dentro da função
# ESCOPO GLOBAL é tudo que está fora da função

# Utilizando uma variável global

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

salario_com_bonus = salario_bonus(500) # 2500
print(salario_com_bonus)
