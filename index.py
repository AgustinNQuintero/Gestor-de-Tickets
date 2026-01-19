import logica

print("Bienvenidos al gestor de tickets")
print("===============================")

id_usuario = int(input("Ingrese su usuario: "))

while True:

    # USUARIO NORMAL
    if id_usuario == 101:
        print("\nSeleccione una opción:")
        print("1. Crear un nuevo ticket")
        print("2. Consultar mis tickets")
        print("3. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            logica.CrearTicket(id_usuario)

        elif opcion == "2":
            logica.ConsultaTickets(id_usuario)

        elif opcion == "3":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida.")


    # ADMIN
    elif id_usuario == 2000:
        print("\nSeleccione una opción:")
        print("1. Ver todos los tickets")
        print("2. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            logica.VerTodosLosTickets()

        elif opcion == "2":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida.")


    # TECNICO
    elif id_usuario == 3000:
        print("\nSeleccione una opción:")
        print("1. Ver tickets asignados")
        print("2. Actualizar estado de ticket")
        print("3. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            logica.ver_tickets_asignados()

        elif opcion == "2":
            logica.actualizar_estado_de_ticket()

        elif opcion == "3":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida.")


    else:
        print("❌ Usuario no reconocido")
        break
