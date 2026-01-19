import logica

print("Bienvenidos al gestor de tickets")
print("===============================")

id_usuario = int(input("Ingrese su ID de usuario: "))
usuario = logica.buscar_usuario_por_id(id_usuario)

if not usuario:
    print("❌ Usuario no encontrado")
    exit()

print(f"✅ Bienvenido {usuario['nombre_usuario']} ({usuario['rango']})")

while True:

    # USUARIO NORMAL
    if usuario["rango"] == "Usuario":
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
    elif usuario["rango"] == "Administrador":
        print("\nSeleccione una opción:")
        print("1. Ver todos los tickets")
        print("2. Asignar ticket a técnico")
        print("3. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            logica.VerTodosLosTickets()

        elif opcion == "2":
            logica.AsignarTicketATecnico()
            break

        else:
            print("Opción no válida.")


    # TECNICO
    elif usuario["rango"] == "Técnico":
        print("\nSeleccione una opción:")
        print("1. Ver tickets asignados")
        print("2. Actualizar estado de ticket")
        print("3. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            logica.ver_tickets_asignados(id_usuario)

        elif opcion == "2":
            logica.actualizar_estado_de_ticket(id_usuario)

        elif opcion == "3":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida.")


    else:
        print("❌ Usuario no reconocido")
        break


