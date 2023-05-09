num = int(input("Ingrese el número a multiplicar: "))
fin = int(input("Ingrese hasta que número se calculará la tabla: "))

for valor in range(1, fin+1, 1):
    print(f'{num} x {valor} = {num * valor}')

print("Hasta Luego")
