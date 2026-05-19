# 5 invertir contraseña
def invertir_contrasena(contrasena) -> str:
    """invierte la contraseña ingresada por el usuario.

    Args:
        (str), cadena de caracteres que ingresa el usuario
    returns:
            (str), retorna la contraseña invertida"""

    contrasena

    con_invertida = ""

    for i in range(len(contrasena) - 1, -1, -1):
        con_invertida += contrasena[i]

    print(f"La contraseña invertida es la siguiente: ({con_invertida})")

    return con_invertida



# 7 Verificar si es palíndromo 
def verificar_palindromo(contrasena) -> str:
    """invierte la contraseña ingresada por el usuario
    y verifica si es palíndromo.

    Args:
        (str) , cadena de caracteres que ingresa el usuario
    returns:
            (str) , retorna el resultado si es palíndromo"""

    contrasena

    contrasena_invertida = ""

    for i in range(len(contrasena) - 1, -1, -1):
        contrasena_invertida += contrasena[i]

    if contrasena_invertida == contrasena:
        print(f"Es palíndromo , la contraseña se lee igual de izquierda a derecha y de derecha a izquierda.")
    else:
        print(f" {contrasena}, NO ES PALÍNDROMO")
    
    resultado = "es palíndromo"

    return resultado



# Buscar carácter específico
def buscar_caracter(contrasena):

    caracter_a_buscar = input("Elija un carácter para buscar en la contraseña ingresada: ")

    contador = 0
    longitud = len(caracter_a_buscar)
    

    for i in range(len(contrasena)):
        if contrasena[i] == caracter_a_buscar:
            contador += 1
            
    print(f"el carácter ('{caracter_a_buscar}') aparece ('{contador}') veces\n")
    if contador != 0:
            print(f"Aparece en la/s posicion/es:\n")
            for i in range(len(contrasena)):
                if contrasena[i] == caracter_a_buscar:
                    posiciones = i
                    print(f"{posiciones}\n")
            
    return



# 8. Ordenar carácteres de la contraseña
def ordenar_caracteres(contrasena):
    """ ordenar los caracteres recibidos por parametro de manera ascendente/descendente.(código ASCII)

    Args:
        (str), cadena de caracteres que ingresa el usuario
    returns:
            (str), retorna la contraseña según ordenamiento """

    
    print("ELIJA EL MODO QUE QUIERA ORDENAR LOS CARACTERES")
    modo = input("1. De manera ascendente\n" 
                    "2. De manera descendente")
    
    if modo == "1":
        contrasena = list(contrasena)
        n = len(contrasena)
        for i in range(n):
            for j in range(n - i - 1):
                if contrasena[j] > contrasena[j + 1]:
                    momentaneo = contrasena[j]
                    contrasena[j] = contrasena[j + 1]
                    contrasena[j + 1] = momentaneo

        resultado = ""
        for i in range(len(contrasena)):
            resultado += contrasena[i]
        

        
    elif modo == "2":
        contrasena = list(contrasena)
        n = len(contrasena)
        for i in range(n):
            for j in range(n - i - 1):
                if contrasena[j] < contrasena[j + 1]:
                    momentaneo = contrasena[j]
                    contrasena[j] = contrasena[j + 1]
                    contrasena[j + 1] = momentaneo

        resultado = ""
        for i in range(len(contrasena)):
            resultado += contrasena[i]
    else:
        print("NO ELEIGIO NINGUNA DE LAS OPCIONES")
    
    
    print(f"{resultado}")
    return resultado
