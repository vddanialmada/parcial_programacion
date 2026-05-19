from validaciones import ingresar_contrasena #1
from validaciones import validar_seguridad #2
from analisis import mostrar_cantidad #3
from utilidades import buscar_caracter #4
from utilidades import invertir_contrasena #5
from analisis import reportar_estadistica #6
from utilidades import verificar_palindromo #7
from utilidades import ordenar_caracteres #8


menu = input(
    "1. Ingresar contraseña\n"
    "2. Validar nivel de seguridad\n"
    "3. Contar tipo de caracteres\n"
    "4. Buscar carácter específico\n"
    "5. Mostrar contraseña invertida\n"
    "6. Generear reporte estadístico\n"
    "7. Verificar si es palíndromo\n"
    "8. Ordenar carácteres de la contraseña\n"
    "9. Salir\n"
)
if menu == "1" or menu == "9":
    match menu:
        case "1":# Ingresar contraseña

            contrasena = input("Ingresar contraseña: \n")


            ingresar_contrasena(contrasena)
        

    opciones = input("¿Desea ejecutar alguna de las otras opciones? si/no: \n\n"
                    )
    
    if opciones == "si":
        menu = input(
            "2. Validar nivel de seguridad\n"
            "3. Contar tipo de caracteres\n"
            "4. Buscar carácter específico\n"
            "5. Mostrar contraseña invertida\n"
            "6. Generear reporte estadístico\n"
            "7. Verificar si es palíndromo\n"
            "8. Ordenar carácteres de la contraseña\n"
            "9. Salir\n"
        )
    else:
        print("gracias por visitarnos")


    match menu:
                           
        case "2": # Validar nivel de seguridad

            validar_seguridad(contrasena)
            

        case "3":# Contar tipos de caracteres

            mostrar_cantidad(contrasena)

           
        case "4":# Buscar carácter específico 

            buscar_caracter(contrasena)


        case "5": # Mostrar contraseña invertida

            invertir_contrasena(contrasena)

                                   
        case "6": #Generar reporte estadístico

            reportar_estadistica(contrasena)

        
        case "7":# Verificar si es palíndromo

            verificar_palindromo(contrasena)

                    
        case "8":# Ordenar caracteres de la contraseña

            ordenar_caracteres(contrasena)  

        
        case "9":
            print("gracias por visitarnos")
else:
     print("Primero debe ingresar una contraseña válida")
