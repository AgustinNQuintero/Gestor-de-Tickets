print ("Bienvenidos al gestor de tickets")
print ("Seleccione una opción:")
print ("1. Crear un nuevo ticket")
print ("2. Ver tickets existentes")
print ("3. Cerrar un ticket")
opcion=input ("Ingrese el número de la opción deseada: ")


while True:  
    if opcion == "1":
        print("Creando un nuevo ticket...")
        # Lógica para crear un nuevo ticket
    elif opcion == "2":
        print("Mostrando tickets existentes...")
        # Lógica para ver tickets existentes
    elif opcion == "3":
        print("Cerrando un ticket...")
        # Lógica para cerrar un ticket  
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
        break