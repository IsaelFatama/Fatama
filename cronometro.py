import os
import time
for horas in range(0,24):
    os.system('cls')
    for minutos in range(0,60):
        os.system('cls')
        for segundos in range(0,60):
            print(f'{horas}:{minutos}:{segundos}')
            time.sleep(1)
            os.system('cls')

print('Hasta Luego')