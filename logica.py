import csv

RUTA_CSV = "data/tickets.csv"
RUTA_USUARIOS_CSV = "data/usuarios.csv"
###User functions


def buscar_usuario_por_id(id_usuario):
    with open(RUTA_USUARIOS_CSV, mode="r", encoding="utf-8") as archivo:
        reader = csv.DictReader(archivo)

        for fila in reader:
            fila = {k.strip(): v.strip() for k, v in fila.items()}

            if int(fila["id"]) == id_usuario:
                return fila

    return None

def generar_id_ticket():
    try:
        with open(RUTA_CSV, mode="r", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)
            filas = list(reader)

            if len(filas) <= 1:
                return 1

            ultimo_id = int(filas[-1][0])
            return ultimo_id + 1

    except FileNotFoundError:
        return 1


def CrearTicket(id_usuario):
    id_ticket = generar_id_ticket()
    titulo = input("Ingrese el título del ticket: ")

    print("Elija la prioridad del ticket:")
    print("1. No puedo realizar mi trabajo")
    print("2. Puedo realizar parte de mi trabajo")
    print("3. Puedo realizar todo mi trabajo")

    prioridad_num = int(input("Ingrese el número de la prioridad: "))

    if prioridad_num == 1:
        prioridad = "Alta"
    elif prioridad_num == 2:
        prioridad = "Media"
    elif prioridad_num == 3:
        prioridad = "Baja"
    else:
        print("❌ Prioridad inválida")
        return

    problema = input("Ingrese la descripción del problema: ")

    with open(RUTA_CSV, mode="a", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)

        # Crear encabezado si el archivo no existe
        if archivo.tell() == 0:
            writer.writerow([
                "id_ticket",
                "id_usuario",
                "titulo",
                "prioridad",
                "problema",
                "estado",
                "tecnico_id"
            ])

        writer.writerow([
            id_ticket,
            id_usuario,
            titulo,
            prioridad,
            problema,
            "Abierto",
            ""
        ])

    print("================================")
    print("✅ Ticket creado con éxito")
    print(f"ID Ticket: {id_ticket}")





def ConsultaTickets(id_usuario):
    with open(RUTA_CSV, mode="r", encoding="utf-8") as archivo:
        reader = csv.reader(archivo)
        next(reader)  # salta encabezado
        encontrados = False

        for fila in reader:
            if len(fila) < 8:
                continue  # evita errores si hay filas rotas

            if int(fila[1]) == id_usuario:
                print(
                    f"ID Ticket: {fila[0]} | "
                    f"Título: {fila[2]} | "
                    f"Prioridad: {fila[3]} | "
                    f"Problema: {fila[4]} | "
                    f"Estado: {fila[5]} | "
                    f"Técnico: {fila[6] or 'Sin asignar'} | "
                    f"Respuesta: {fila[7] or 'Sin respuesta'}"
                )
                encontrados = True

        if not encontrados:
            print("📭 No tenés tickets registrados.")



###Admin functions

def VerTodosLosTickets():
    with open(RUTA_CSV, mode="r", encoding="utf-8") as archivo:
        reader = csv.reader(archivo)
        for fila in reader:
            print(
                f"Usuario: {fila[1]} | "
                f"Título: {fila[2]} | "
                f"Prioridad: {fila[3]} | "
                f"Problema: {fila[4]} | "
                f"Estado: {fila[5]} |"
                f"Técnico Asignado: {fila[6]} |"
                f"Respuesta: {fila[7]}"
            )



def es_tecnico(tecnico_id):
    with open(RUTA_USUARIOS_CSV, mode="r", encoding="utf-8") as archivo:
        reader = csv.reader(archivo)
        next(reader)
        for fila in reader:
            if int(fila[0]) == tecnico_id and fila[2] == "Técnico":
                return True
    return False
            
            

def AsignarTicketATecnico():
    ticket_id = int(input("Ingrese el ID del ticket: "))
    tecnico_id = int(input("Ingrese el ID del técnico: "))

    if not es_tecnico(tecnico_id):
        print("❌ El ID ingresado no corresponde a un técnico")
        return

    with open(RUTA_CSV, mode="r", encoding="utf-8") as archivo:
        reader = csv.reader(archivo)
        encabezado = next(reader)
        tickets = list(reader)

    encontrado = False

    for ticket in tickets:
        if int(ticket[0]) == ticket_id:
            ticket[6] = tecnico_id
            encontrado = True
            break

    if not encontrado:
        print("❌ Ticket no encontrado")
        return

    with open(RUTA_CSV, mode="w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(encabezado)
        writer.writerows(tickets)

    print(f"✅ Ticket {ticket_id} asignado al técnico {tecnico_id}")







###Tecnico functions

def ver_tickets_asignados(id_usuario):
    with open(RUTA_CSV, mode="r", encoding="utf-8") as archivo:
        reader = csv.reader(archivo)
        next(reader)  # salta encabezado
        encontrados = False

        for fila in reader:
            if len(fila) < 8:
                continue  # evita filas corruptas

            if fila[6] != "" and int(fila[6]) == id_usuario:
                print(
                    f"ID Ticket: {fila[0]} | "
                    f"Título: {fila[3]} | "
                    f"Prioridad: {fila[2]} | "
                    f"Problema: {fila[4]} | "
                    f"Estado: {fila[5]} | "
                    f"Técnico: {fila[6]} | "
                    f"Respuesta: {fila[7] or 'Sin respuesta'}"
                )
                encontrados = True

        if not encontrados:
            print("📭 No tenés tickets asignados.")


def actualizar_estado_de_ticket(id_usuario):
    tickets = []

    with open(RUTA_CSV, mode="r", encoding="utf-8") as archivo:
        reader = csv.reader(archivo)
        header = next(reader)
        tickets.append(header)

        for fila in reader:
            tickets.append(fila)

    print("\n📋 Tus tickets asignados:")
    for fila in tickets[1:]:
        if fila[6] and int(fila[6]) == id_usuario:
            print(f"ID Ticket: {fila[0]} | Estado: {fila[5]} | Título: {fila[3]}")

    ticket_id = input("\nIngrese el ID del ticket a actualizar: ")

    encontrado = False

    for fila in tickets[1:]:
        if fila[0] == ticket_id and fila[6] == str(id_usuario):
            print("\nSeleccione nuevo estado:")
            print("1. Abierto")
            print("2. En proceso")
            print("3. Cerrado")

            opcion = input("Opción: ")

            if opcion == "1":
                fila[5] = "Abierto"
            elif opcion == "2":
                fila[5] = "En proceso"
            elif opcion == "3":
                fila[5] = "Cerrado"
            else:
                print("❌ Opción inválida")
                return

            fila[7] = input("Ingrese respuesta del técnico: ")
            encontrado = True
            break

    if not encontrado:
        print("❌ Ticket no encontrado o no asignado a usted")
        return

    with open(RUTA_CSV, mode="w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerows(tickets)

    print("✅ Ticket actualizado con éxito")

    