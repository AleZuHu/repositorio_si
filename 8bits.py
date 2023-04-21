def add8(a0,a1,a2,a3,a4,a5,a6,a7,b0,b1,b2,b3,b4,b5,b6,b7,c0):
    # Inicializamos s1 a False
    s1 = False
    # Comparamos a0 con b0, y luego ese resultado con c0.
    # Si son diferentes, asignamos True a s1.
    if (a0 != b0) != c0:
        s1 = True
    # Inicializamos c1 a False
    c1 = False
    # Calculamos el valor de c1 mediante una operación lógica de and y xor.
    # Si a0 y b0 son True y c0 y (a0 != b0) son diferentes, entonces c1 es True.
    if (a0 and b0) != (c0 and (a0 != b0)):
        c1 = True
    # Repetimos el mismo proceso para s2-s8 y c2-c8.
    s2 = False
    if (a1 != b1) != c1:
        s2 = True
    c2 = False
    if (a1 and b1) != (c1 and (a1 != b1)):
        c2 = True
    s3 = False
    if (a2 != b2) != c2:
        s3 = True
    c3 = False
    if (a2 and b2) != (c2 and (a2 != b2)):
        c3 = True
    s4 = False
    if (a3 != b3) != c3:
        s4 = True
    c4 = False
    if (a3 and b3) != (c3 and (a3 != b3)):
        c4 = True
    s5 = False
    if (a4 != b4) != c4:
        s5 = True
    c5 = False
    if (a4 and b4) != (c4 and (a4 != b4)):
        c5 = True
    s6 = False
    if (a5 != b5) != c5:
        s6 = True
    c6 = False
    if (a5 and b5) != (c5 and (a5 != b5)):
        c6 = True
    s7 = False
    if (a6 != b6) != c6:
        s7 = True
    c7 = False
    if (a6 and b6) != (c6 and (a6 != b6)):
        c7 = True
    s8 = False
    if (a7 != b7) != c7:
        s8 = True
    c8 = False
    if (a7 and b7) != (c7 and (a7 != b7)):
        c8 = True
    # Devolvemos una tupla con los valores de s1-s8 y c8
    return (s1,s2,s3,s4,s5,s6,s7,s8,c8)
    
def test():
    # Se realiza un bucle anidado que recorre todas las posibles combinaciones de valores booleanos para cada variable
    for a0 in [False, True]:
        for a1 in [False, True]:
            for a2 in [False, True]:
                for a3 in [False, True]:
                    for a4 in [False, True]:
                        for a5 in [False, True]:
                            for a6 in [False, True]:
                                for a7 in [False, True]:
                                    for b0 in [False, True]:
                                        for b1 in [False, True]:
                                            for b2 in [False, True]:
                                                for b3 in [False, True]:
                                                    for b4 in [False, True]:
                                                        for b5 in [False, True]:
                                                            for b6 in [False, True]:
                                                                for b7 in [False, True]:
                                                                    for c0 in [False, True]:
                                                                        # Se llama a la función add8() con los valores actuales de las variables
                                                                        add8(a0,a1,a2,a3,a4,a5,a6,a7,b0,b1,b2,b3,b4,b5,b6,b7,c0)

test()
