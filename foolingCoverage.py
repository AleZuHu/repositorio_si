import math # Importamos el módulo math para usar la función abs() que devuelve el valor absoluto de un número.

def stats(lst):
    min = None # Inicializamos la variable min con el valor None.
    max = None # Inicializamos la variable max con el valor None.
    freq = {} # Inicializamos el diccionario freq vacío.
    # Recorremos cada elemento de la lista.
    for i in lst:
        i = abs(i) # Obtenemos el valor absoluto de i.
        # Comprobamos si el valor actual es menor que el mínimo actual o si min es None.
        if min is None or i < min:
            min = i # Si se cumple, actualizamos el valor de min.
        # Comprobamos si el valor actual es mayor que el máximo actual o si max es None.
        if max is None or i > max:
            max = i # Si se cumple, actualizamos el valor de max.
        # Comprobamos si el valor actual ya existe en el diccionario freq.
        if i in freq:
            freq[i] += 1 # Si se cumple, incrementamos en 1 el valor correspondiente en el diccionario.
        else:
            freq[i] = 1 # Si no se cumple, añadimos el valor al diccionario con un valor inicial de 1.
    lst_sorted = sorted(lst) # Ordenamos la lista.
    # Comprobamos si la lista tiene un número par de elementos.
    if len(lst_sorted)%2 == 0:
        middle = len(lst_sorted)/2 # Obtenemos el índice del elemento que está en la mitad de la lista.
        median = (lst_sorted[middle] + lst_sorted[middle-1]) / 2 # Calculamos la mediana como la media aritmética 
                                                                 # de los dos valores que están en el centro de la lista.
    else:
        median = lst_sorted[len(lst_sorted)/2] # Si la lista tiene un número impar de elementos, 
                                            #la mediana es el valor que está en el centro.
    mode_times = None # Inicializamos la variable mode_times con el valor None.
    # Recorremos los valores del diccionario freq.
    for i in freq.values():
        # Comprobamos si el valor actual es mayor que mode_times o si mode_times es None.
        if mode_times is None or i > mode_times:
            mode_times = i # Si se cumple, actualizamos el valor de mode_times.
    mode = [] # Inicializamos la lista mode vacía.
    # Recorremos los elementos del diccionario freq.
    for (num, count) in freq.items():
        # Comprobamos si el valor de count es igual a mode_times.
        if count == mode_times:
            mode.append(num) # Si se cumple, añadimos el valor de num a la lista mode.
    print("lista = " + str(lst))  # Imprimimos la lista original.
    print("mínimo = " + str(min))  # Imprimimos el valor mínimo.
    print("máximo = " + str(max))  # Imprimimos el valor máximo.
    print("mediana = " + str(median))  # Imprimimos la mediana.
    print("moda(s) = " + str(mode))   # Imprimimos la(s) moda(s).

def test1():
    l = [1,2,3]
    stats(l)
    l = [-1,-2,-3]
    stats(l)
    l = [31,32,33,34]
    stats(l)
    l = [31,32,33]
    stats(l)
    l = [31,32,33,33,34]
    stats(l)
    l = [31,31,32,33,33,34]
    stats(l)
def test2():
    l = [-1,2,3]
    stats(l)
    l = [1,-2,-3]
    stats(l)
    l = [31,-32,33,-34]
    stats(l)
    l = [31,32,-33]
    stats(l)
    l = [-31,32,33,33,-34]
    stats(l)
    l = [-31,-31,32,33,33,-34]
    stats(l)

test1()
test2()