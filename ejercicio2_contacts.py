class Contact:  # Definimos la clase y el nombre de la clase
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

def show_menu():
    print("\n Gestión de contactos")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

notebook = []

def add_contact():
    name = input("Ingresa el nombre del contacto: ")
    phone = input("Ingresa el número de teléfono del contacto: ")
    notebook.append(Contact(name, phone))
    print("Contacto agregado exitosamente")
    input("Presiona Enter para continuar...")

def show_contacts():
    if notebook:
        for contact in notebook:
            print(f'Nombre: {contact.name}, Teléfono: {contact.phone}')
            input("Presiona Enter para continuar...")
    else:
        print("No hay contactos para mostrar.")
        input("Presiona Enter para continuar...")

def search_contact():
    name = input("Ingrese el nombre que desea buscar: ")
    for contact in notebook:
        if contact.name == name:
            print(f'Nombre: {contact.name}, Teléfono: {contact.phone}')
            input("Presiona Enter para continuar...")
            return
    print("Contacto no encontrado.")
    input("Presiona Enter para continuar...")

def delete_contact():
    name = input("Ingrese el nombre que desea eliminar: ")
    for contact in notebook:
        if contact.name == name:
            notebook.remove(contact)
            print("Contacto eliminado")
            input("Presiona Enter para continuar...")
            return
    print("Contacto no encontrado.")
    input("Presiona Enter para continuar...")

while True:
    show_menu()
    option = input("Elige una opción: ")

    match option:
        case "1":
            add_contact()
        case "2":
            show_contacts()
        case "3":
            search_contact()
        case "4":
            delete_contact()
        case "5":
            print("Ha salido del programa.")
            break
        case _:
            print("Opción no válida. Intente nuevamente.")