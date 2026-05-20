# 1 contrasena 

def ingresar_contrasena(contrasena) -> str:
    """
    se encarga de validar las contraseñas ingresadas por el usuario 

    Args:
        (str) , cadena de caracteres que ingresa el usuario
    returns:
            (str) , retorna la contraseña válida
    """

    validacion = 1

    while validacion != 0:

        validacion = 0

        if contrasena == "":
            print("La contraseña no puede estar vacía\n")
            validacion += 1

        elif len(contrasena) < 8:
            print("La contraseña debe tener mínimo 8 caracteres\n")
            validacion += 1

        elif contrasena[0] == " ":
            print("La contraseña no puede comenzar con espacio vacío\n")
            validacion += 1

        else:
            letras = 0
            buscar_letra = (
                "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
            )

            for i in range(len(contrasena)):
                for j in range(len(buscar_letra)):
                    if contrasena[i] == buscar_letra[j]:
                        letras += 1

            if letras == 0:
                print("Debe contener al menos una letra\n")
                validacion += 1

            else:

                print("Contraseña válida: ",end="")
                print(f"{contrasena}")


                return contrasena

        contrasena = input("Ingresar contraseña: \n")



# 2 Validar nivel de seguridad:
def validar_seguridad(contrasena) -> str:
    """evalua el nivel de seguridad segun la cantidad y tipo de caracteres
        que contiene la contraseña ingresada por el usuario

    Args:
        (str) , cadena de caracteres que ingresa el usuario
    returns:
            (str) , retorna el nivel de seguri
    """

    cantidad_letras = contrasena
    cantidad_numeros = contrasena
    cantidad_simbolos = contrasena
    buscar_letra = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    buscar_numero = "0123456789"
    buscar_sim = "!“#$%&()*+,-./"
    largo = 0
    letras = 0
    numero = 0
    simbolo = 0
    evaluacion = ""


    for i in range(len(cantidad_letras)):
        largo += 1

    
    for i in range(len(cantidad_letras)):
        for j in range(len(buscar_letra)):
            if cantidad_letras[i] == buscar_letra[j]:
                letras += 1  


    for i in range(len(cantidad_numeros)):
        for j in range(len(buscar_numero)):
            if cantidad_numeros[i] == buscar_numero[j]:
                numero += 1


    for i in range(len(cantidad_simbolos)):
        for j in range(len(buscar_sim)):
            if cantidad_simbolos[i] == buscar_sim[j]:
                simbolo += 1



    if 8 <= largo <= 9 and largo == letras:
        evaluacion = "Débil"
        print(f"Nivel de seguridad '{evaluacion}' su contraseña contiene {largo} caracteres y son todos letras")


    elif 8 <= largo <= 9 and letras != 0 and numero != 0:
        evaluacion = "Media"
        print(f"Nivel de seguridad '{evaluacion}' su contraseña contiene {largo} caracteres. Son números y letras")


    elif largo >= 12 and simbolo !=0 and letras != 0 and numero != 0:
        evaluacion = "Fuerte"
        print(f"Nivel de seguridad '{evaluacion}' su contraseña contiene {largo} caracteres. Son números, símbolos y letras")    



    return evaluacion

