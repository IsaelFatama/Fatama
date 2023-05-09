def esPrimo(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

while True:
    n = int(input("Ingrese un número para verificar si es primo (o ingrese 0 para salir): "))
    if n == 0:
        break
    if esPrimo(n):
        print(f"{n} es primo.")
    else:
        print(f"{n} no es primo.")
