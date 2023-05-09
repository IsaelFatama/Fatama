import os
import time

horas = int(input("Introduce las horas: "))
minutos = int(input("Introduce los minutos: "))
segundos = int(input("Introduce los segundos: "))

total_segundos = horas*3600 + minutos*60 + segundos

while total_segundos >= 0:
    os.system('cls')
    mins, segs = divmod(total_segundos, 60)
    hrs = 0
    if mins >= 60:
        hrs, mins = divmod(mins, 60)
    print(f'{hrs:02d}:{mins:02d}:{segs:02d}')
    time.sleep(1)
    total_segundos -= 1

print('Tiempo Finalizado')
