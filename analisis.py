
# 3 Contar tipos de caracteres:
def mostrar_cantidad(contrasena) -> str:
    """muestra las cantidad y tipo de caracteres
        que contiene la contraseña ingresada por el usuario

    Args:
        (str) , cadena de caracteres que ingresa el usuario
    returns:
            (str) , retorna la contraseña válida
    """

    # cantidad de letras,
    cantidad_letras = contrasena
    buscar_letra = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    cantidad = 0

    for i in range(len(cantidad_letras)):
        for j in range(len(buscar_letra)):
            if cantidad_letras[i] == buscar_letra[j]:
                cantidad += 1

    print(f"Aparecen {cantidad} letras en la contraseña")

    # cantidad de números,
    cantidad_numeros = contrasena
    buscar_numero = "0123456789"
    cantidad = 0

    for i in range(len(cantidad_numeros)):
        for j in range(len(buscar_numero)):
            if cantidad_numeros[i] == buscar_numero[j]:
                cantidad += 1

    print(f"Aparecen {cantidad} números en la contraseña")

    # cantidad de símbolos,
    cantidad_simbolos = contrasena
    buscar_sim = "°!#$%&/()=?¡*¨{[}]"
    cantidad = 0

    for i in range(len(cantidad_simbolos)):
        for j in range(len(buscar_sim)):
            if cantidad_simbolos[i] == buscar_sim[j]:
                cantidad += 1

    print(f"Aparecen {cantidad} símbolos en la contraseña")

    # cantidad de espacios.
    cantidad_espacios = contrasena
    lugar_vacio = " "
    cantidad = 0

    for i in range(len(cantidad_espacios)):
        for j in range(len(lugar_vacio)):
            if cantidad_espacios[i] == lugar_vacio[j]:
                cantidad += 1

    print(f"Aparecen {cantidad} espacios en la contraseña")

    return




# 6. Generear reporte estadístico
def reportar_estadistica(contrasena) -> str:
    """muestra muestra el porcentaje de cada tipo de caracteres
        que contiene la contraseña ingresada por el usuario

    Args:
        (str) , cadena de caracteres que ingresa el usuario
    returns:
            (str) , retorna los resultados de cada estadistica
    """

    # longitud total
    longitud = 0

    for i in contrasena:
        longitud += 1

    print(f"La longitud de la contraseña es: {longitud}")

    # cantidad de letras,
    cantidad_letras = contrasena
    buscar_letra = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    cantidad = 0

    for i in range(len(cantidad_letras)):
        for j in range(len(buscar_letra)):
            if cantidad_letras[i] == buscar_letra[j]:
                cantidad += 1
                porcentaje_letras = (cantidad / (len(contrasena))) * 100

    print(f"El porcentaje de letras ingresadas es: {porcentaje_letras}%")

    # cantidad de números,
    cantidad_numeros = contrasena
    buscar_numero = "0123456789"
    cantidad = 0

    for i in range(len(cantidad_numeros)):
        for j in range(len(buscar_numero)):
            if cantidad_numeros[i] == buscar_numero[j]:
                cantidad += 1
            porcentaje_numeros = (cantidad / (len(contrasena))) * 100

    print(f"El porcentaje de números ingresadas es: {porcentaje_numeros}%")

    # cantidad de símbolos,
    cantidad_simbolos = contrasena
    buscar_sim = "°!#$%&/()=?¡*¨{[}]"
    cantidad = 0

    for i in range(len(cantidad_simbolos)):
        for j in range(len(buscar_sim)):

            if cantidad_simbolos[i] == buscar_sim[j]:
                cantidad += 1

            else:
                (f"El porcentaje de simbolos ingresadas es: {cantidad}")

            porcentaje_simbolos = (cantidad / (len(contrasena))) * 100

    print(f"El porcentaje de simbolos ingresadas es: {porcentaje_simbolos}%")
    # Letras repetidas
    letra_repetida = ""

    contrasena

    for i in range(len(contrasena) - 1):
        cantidad_repeticiones = 0


        if contrasena[i] == contrasena[i + 1]:
            cantidad_repeticiones += 1
            # letra_repetida += contrasena[i]
                

            print(
                f"Se repite: ({cantidad_repeticiones}) veces la letra: ({contrasena[i]})"
            )

    return (
        longitud,
        porcentaje_letras,
        porcentaje_numeros,
        porcentaje_simbolos,
        cantidad_repeticiones,
        letra_repetida,
    )
