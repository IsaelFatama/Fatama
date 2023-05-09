while True:
    try:
        num = int(input("Ingrese el número a multiplicar: "))
        fin = int(input("Ingrese hasta qué número se calculará la tabla: "))

        if num <= 0 or fin < num:
            raise ValueError("Ingrese un número válido y un límite superior mayor o igual al número ingresado.")

        break
    except ValueError:
        print("Ha ocurrido un error. Ingrese valores numéricos válidos.")

for valor in range(1, fin + 1):
    print(f'{num} x {valor} = {num * valor}')

print("Se ha mostrado la tabla de multiplicar correctamente. ¡Hasta luego!")
