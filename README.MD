🎫 Gestor de Tickets en Python

Sistema de gestión de tickets desarrollado en Python, orientado a la práctica de buenas prácticas de programación, manejo de archivos CSV, modularización y control de flujo según roles de usuario.

El proyecto simula un entorno real de soporte técnico, donde distintos tipos de usuarios interactúan con el sistema según su rol.

🧠 Descripción general

El Gestor de Tickets permite:

Crear tickets de soporte

Consultar tickets propios

Visualizar todos los tickets del sistema

Asignar tickets a técnicos

Visualizar tickets asignados a cada técnico

Actualizar el estado de un ticket

Toda la información se almacena en archivos CSV, evitando el uso de bases de datos para mantener el proyecto simple y enfocado en la lógica.

👥 Roles del sistema

El acceso y las funcionalidades dependen del rango del usuario, obtenido desde un archivo CSV:

Rol	Funcionalidades
Usuario	Crear tickets, consultar sus propios tickets
Administrador	Ver todos los tickets, asignar tickets a técnicos
Técnico	Ver tickets asignados, actualizar estado y respuesta


📁 Estructura del proyecto
```bash
Gestor-de-Tickets/
│
├── index.py                 # Punto de entrada del sistema (menús y flujo)
├── logica.py                # Lógica principal del sistema
│
├── data/
│   ├── tickets.csv          # Tickets del sistema
│   └── usuarios.csv         # Usuarios y roles
│
├── README.md

```

🗂️ Archivos CSV
📄 usuarios.csv
```bash
id,nombre_usuario,rango
101,juanp,Usuario
102,marial,Usuario
103,carloss,Usuario
2000,admin,Administrador
3000,tecnico1,Técnico
```

📄 tickets.csv (estructura)
```bash
id_ticket,id_usuario,nombre_usuario,prioridad,titulo,problema,estado,tecnico_asignado,respuesta
```

▶️ Cómo ejecutar el proyecto

Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/gestor-de-tickets.git
```

Ingresar al proyecto:
```bash
cd gestor-de-tickets
```

Ejecutar el programa:
```bash
python index.py
```


🎯 Objetivos del proyecto

Practicar programación estructurada y modular

Comprender el flujo de un sistema real

Manejo de archivos CSV con csv

Separación de responsabilidades

Simulación de autenticación y control por roles


👤 Autor:
🆔Agustín Nicolás Quintero.
📌 Cordoba,Argentina.