import math
def isPrime(number):
    # El número 2 es el único número primo par.
    # Por lo tanto, si el número es 2, se devuelve True.
    if number == 2:
        return True
    # Los números negativos, cero y 1 no son primos.
    # Además, los números pares diferentes de 2 tampoco son primos.
    # Por lo tanto, se devuelve False para estos casos.
    if number <= 1 or (number % 2) == 0:
        return False
    # Se verifica si el número es divisible por algún número impar menor a la raíz cuadrada del número.
    # Si se encuentra algún divisor, entonces el número no es primo y se devuelve False.
    # Si no se encuentra ningún divisor, entonces el número es primo y se devuelve True.
    for check in range(3, int(math.sqrt(number))):
        if (number % check) == 0:
            return False
    return True

# Función para verificar si un número es primo (versión optimizada)
def isPrime2(number):
    # El número 2 es el único número primo par.
    # Por lo tanto, si el número es 2, se devuelve True.
    if number == 2:
        return True
    # Los números negativos, cero y 1 no son primos.
    # Además, los números pares diferentes de 2 tampoco son primos.
    # Por lo tanto, se devuelve False para estos casos.
    if number <= 1 or (number % 2) == 0:
        return False
    # Se verifica si el número es divisible por algún número impar menor o igual a la raíz cuadrada del número.
    # Si se encuentra algún divisor, entonces el número no es primo y se devuelve False.
    # Si no se encuentra ningún divisor, entonces el número es primo y se devuelve True.
    for check in range(3, int(math.sqrt(number))+1, 2):
        if (number % check) == 0:
            return False
    return True

# Función para probar las funciones isPrime y isPrime2
def test():
    # Se realizan una serie de pruebas para verificar el correcto funcionamiento de las funciones.
    assert isPrime(1) == False
    assert isPrime(2) == True
    assert isPrime(3) == True
    assert isPrime(4) == False
    assert isPrime(5) == True
    assert isPrime(20) == False
    assert isPrime(21) == False
    assert isPrime(22) == False
    assert isPrime(23) == True
    assert isPrime(24) == False

    assert isPrime2(1) == False
    assert isPrime2(2) == True
    assert isPrime2(3) == True
    assert isPrime2(4) == False
    assert isPrime2(5) == True
    assert isPrime2(20) == False
    assert isPrime2(21) == False
    assert isPrime2(22) == False
    assert isPrime2(23) == True
    assert isPrime2(24) == False

# Se llama a la función test para realizar las pruebas.
test()
