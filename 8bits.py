c1:
        s2 = True
    c2 = False
    if (a1 and b1) != (c1 and (a1 != b1)):
        c2 = True
    s3 = False
    if 
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
