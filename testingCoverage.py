def stats(lst):
    min = None                # Inicializamos la variable min como None
    max = None                # Inicializamos la variable max como None
    freq = {}                 # Inicializamos el diccionario freq como vacío
    for i in lst:             # Iteramos a través de la lista lst
        if min is None or i > min:  # Si min es None o i es menor que min (error intencional cambio de signo)
            min = i           # entonces establecemos min como i
        if max is None or i > max:  # Si max es None o i es mayor que max
            max = i           # entonces establecemos max como i
        if i in freq:              # Si i ya se encuentra en el diccionario freq
            freq[i] += 1      # aumentamos su valor en 1
        else:                      # Si i no se encuentra en el diccionario freq
            freq[i] = 1       # lo agregamos al diccionario y lo establecemos como 1
    lst_sorted = sorted(lst)   # Ordenamos la lista lst y la asignamos a lst_sorted
    if len(lst_sorted)%2 == 0:  # Si la longitud de lst_sorted es par
        middle = len(lst_sorted)/2   # calculamos el índice del medio
        median = (lst_sorted[middle] + lst_sorted[middle-1]) / 2  # calculamos la mediana
    else:                     # Si la longitud de lst_sorted es impar
        median = lst_sorted[len(lst_sorted)//2]    # entonces la mediana es el valor en el índice del medio
    mode_times = None          # Inicializamos mode_times como None
    for i in freq.values():    # Iteramos a través de los valores del diccionario freq
        if mode_times is None or i > mode_times:   # Si mode_times es None o i es mayor que mode_times
            mode_times = i    # entonces establecemos mode_times como i
    mode = []                 # Inicializamos la lista mode como vacía
    for (num, count) in freq.items():    # Iteramos a través de los elementos del diccionario freq
        if count == mode_times:           # Si el valor coincide con mode_times
            mode.append(num)            # lo agregamos a la lista mode
    print("lista = " + str(lst))  # Imprimimos la lista lst
    print("mínimo = " + str(min)) # Imprimimos el valor mínimo
    print("máximo = " + str(max)) # Imprimimos el valor máximo
    print("mediana = " + str(median)) # Imprimimos la mediana
    print("moda(s) = " + str(mode))   # Imprimimos la moda

def test():
    l1 = [1, 2, 3, 4, 5]
    stats(l1)

    l2 = [5, 4, 3, 2, 1]
    stats(l2)

    l3 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
    stats(l3)

    l4 = [10, 20, 30]
    stats(l4)

    l5 = [10]
    stats(l5)

    l6 = [1, 2, 3, 4]
    stats(l6)

    l7 = [1, 2, 3, 4, 5, 6]
    stats(l7)

test()


