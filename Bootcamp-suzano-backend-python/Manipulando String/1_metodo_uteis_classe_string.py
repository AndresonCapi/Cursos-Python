##############################
### MAIÚSCULA, MINÚSCULA E TÍTULO ###

curso = "pYthon"

print(curso.upper())
# >>> PYTHON - convertendo todas a letras para maiúscula

print(curso.lower())
# >>> python - convertendo todas a letras para minúsculas

print(curso.title())
#  >>> Python - convertendo apenas a primeira letra para maiúscula

#####################################
###  ELIMINANDO ESPAÇOS EM BRANCO ###

print(curso.strip()) 
#  >>> "Python"  removendo espaços em branco

print(curso.lstrip()) 
#  >>> "Python"  removendo espaço da direita

print(curso.strip()) 
#  >>> "Python"  removendo espaços da esquerda

#####################################
###  JUNÇOES E CENTRALIZAÇÃO ###

curso = "python"

print(curso.center(10, "#"))
# >>> "##Python##"

print(".".join(curso))
# >>> "P.y.t.h.o.n"


