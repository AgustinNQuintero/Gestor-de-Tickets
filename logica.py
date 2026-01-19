import csv

RUTA_CSV = "data/tickets.csv"


def CrearTicket(id_usuario):
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
        print("❌ Opción no válida")
        return

    problema = input("Ingrese la descripción del problema: ")

    with open(RUTA_CSV, mode="a", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow([id_usuario, titulo, prioridad, problema, "Abierto"])

    print("✅ Ticket creado con éxito")


def VerTodosLosTickets():
    with open(RUTA_CSV, mode="r", encoding="utf-8") as archivo:
        reader = csv.reader(archivo)
        for fila in reader:
            print(
                f"Usuario: {fila[0]} | "
                f"Título: {fila[1]} | "
                f"Prioridad: {fila[2]} | "
                f"Problema: {fila[3]} | "
                f"Estado: {fila[4]}"
            )


def ConsultaTickets(id_usuario):
    with open(RUTA_CSV, mode="r", encoding="utf-8") as archivo:
        reader = csv.reader(archivo)
        next(reader) 
        encontrados = False

        for fila in reader:
            if int(fila[0]) == id_usuario:
                print(
                    f"Título: {fila[1]} | "
                    f"Prioridad: {fila[2]} | "
                    f"Problema: {fila[3]} | "
                    f"Estado: {fila[4]}"
                )
                encontrados = True

        if not encontrados:
            print("📭 No tenés tickets registrados.")


def ver_tickets_asignados():
    print("Mostrando tickets asignados al técnico (pendiente de implementar)")


def actualizar_estado_de_ticket():
    ticket_id = int(input("Ingrese el ID del ticket a actualizar: "))
    nuevo_estado = input("Ingrese el nuevo estado del ticket: ")
    print(f"Ticket {ticket_id} actualizado a estado: {nuevo_estado} (pendiente de guardar)")
