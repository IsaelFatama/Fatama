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
        

for i in range(-10, 101):
    print(1, "", esPrimo(1))