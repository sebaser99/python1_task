"""
Ejercicio proyecto 4: Gestion de tareas
"""

class Task:
    def __init__(self, title, description, status):
        self.title = title
        self.description = description
        self.status = status

def show_menu():
    print("\nGestión de Tareas")
    print("1. Agregar Tarea")
    print("2. Mostrar las Tareas")
    print("3. Buscar Tarea")
    print("4. Actualizar Estado Tarea")
    print("5. Eliminar Tarea por Título")
    print("6. Salir")
    
tasks = []

def add_task():
    title = input("Ingresa el título de la tarea: ")
    description = input("Ingresa la descripción de la tarea: ")
    try:
        status = input("¿La tarea está completada? (True/False): ").strip().capitalize()
        if status not in ["True", "False"]:
            raise ValueError("Debe ingresar 'True' o 'False'.")
        status = status == "True"
        task = Task(title, description, status)
        tasks.append(task)
        print("Tarea agregada exitosamente.")
    except ValueError as e:
        print(f"Error: {e}")
    input("Presiona Enter para continuar...")

def show_tasks():
    if tasks:
        for i in tasks:
            print(f'Título: {i.title}, Descripción: {i.description}, Estado: {"Completada" if i.status else "Pendiente"}')
        input("Presiona Enter para continuar...")
    else:
        print("No hay tareas para mostrar.")
        input("Presiona Enter para continuar...")    

def found_task():
    title = input("Ingrese el título de la tarea: ")
    exist = False
    
    for i in tasks:
        if i.title == title:
            print(f'Título: {i.title}, Descripción: {i.description}, Estado: {"Completada" if i.status else "Pendiente"}')
            exist = True
            input("Presiona Enter para continuar...")
            break
    if not exist:
        print("Tarea no encontrada.")
        input("Presiona Enter para continuar...")
    
def update_task_status():
    title = input("Ingrese el título de la tarea a la que desea actualizarle el estado: ")
    exist = False
    
    for i in tasks:
        if i.title == title:
            print("Información actual de la tarea")
            print(f'Título: {i.title}, Descripción: {i.description}, Estado: {"Completada" if i.status else "Pendiente"}')
            try:
                status = input("Ingresa el nuevo estado de la tarea (True/False): ").strip().capitalize()
                if status not in ["True", "False"]:
                    raise ValueError("Debe ingresar 'True' o 'False'.")
                i.status = status == "True"
                print("Información luego de actualizar el estado de la tarea")
                print(f'Título: {i.title}, Descripción: {i.description}, Estado: {"Completada" if i.status else "Pendiente"}')
            except ValueError as e:
                print(f"Error: {e}")
            exist = True
            break
    if not exist:
        print("Tarea no encontrada.")
    input("Presiona Enter para continuar...")
        
def remove_task():
    title = input("Ingrese el nombre de la tarea que desea eliminar: ")
    exist = False
    for i in tasks:
        if i.title == title:
            tasks.remove(i)
            print("Tarea eliminada")
            exist = True
            break
    if not exist:
        print("Tarea no encontrada.")
    input("Presiona Enter para continuar...")
           
while True:
    show_menu()    
    option = input("Elige una opción del menú: ")
           
    match option:
        case "1":
            add_task()
        case "2":
            show_tasks()
        case "3":
            found_task()
        case "4":
            update_task_status()
        case "5":
            remove_task()
        case "6":
            print("Ha salido del programa.")
            break
        case _:
            print("Opción no válida. Intente nuevamente.")