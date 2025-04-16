#  MODULO datetime

# Introdução ao módulo datetime
'''
O módulo 'datetime' em Python é usado para lidar com datas e horas.
Ele possui várias clases úteis como data, time e timedelta.

'''
import datetime

d = datetime.date(2023, 7, 19)
print(d)  # 2023/07/19

from datetime import date, datetime

data = date(2023, 7, 2)
print(data)

# Retornar data do dia
print(date.today())

# Retornando data e hora atual
data_hora = datetime(2023, 5, 10)
print(data_hora)
print(datetime.today())


# Manipulação de datas e horas
from datetime import datetime, timedelta

tipo_carro = "P"  # P, M, G

tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou às: {data_atual} e ficará pronto às {data_estimada}")

elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro chegou às: {data_atual} e ficará pronto às {data_estimada}")

else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")


# Conversão e formatação de datas e horas
'''
Python também permite converter e formatar datas e horas.
Para isso, usamos os métodos 'strftime' (strint format time) e
'strptime' (string parse time).
'''
from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2023-10-20 10:20"
mascara_ptbr = "%d/%m/%y"
mascara_en = "%Y-%m-%d %H:%M"

# Formatando data e hora
print(data_hora_atual.strftime(mascara_ptbr))

# Convertendo string para datetime
print(datetime.strptime(data_hora_str, mascara_en))

# Trabalhando com timezones
from datetime import datetime
import pytz

data1 = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(f'O horário da Noruega é: {data1}')
print(f'O horário de São Paulo é: {data2}')

