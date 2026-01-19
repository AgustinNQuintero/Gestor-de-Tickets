
def CrearTicket():
    id_usuario = int(input("Ingrese el ID del usuario: "))
    
    
    
    print("elija la prioridad del ticket:")
    print("1. No puedo realizar mi trabajo")
    print("2. puedo realizar parte de mi trabajo")
    print("3. puedo realizar todo mi trabajo")
    prioridad = int(input("Ingrese el número de la prioridad: "))
    
    if prioridad > 3 or prioridad < 1:
        print("Opcion no valida")
        return
    
    problema = input("Ingrese la descripción del problema: ")
    
    
    print("================================")
    print("Ticket creado con éxito")
    print(f"Usuario: {id_usuario}")
    print(f"Prioridad: {prioridad}")
    print(f"Problema: {problema}")
    
    
    
    CrearTicket()