"""
Ejercicio proyecto 3: Gestion de inventarios
"""

class Product: 
    def __init__(self, name, cant, price):
        self.name = name
        self.cant = cant
        self.price = price

def show_menu():
    print("\n Sistema de inventarios")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Actualizar cantidad producto")
    print("5. Eliminar producto")
    print("6. Salir")
    
stock = []

def add_product():
    name = input("Ingresa el nombre del producto: ")
    try:
        cant = int(input("Ingresa la cantidad del producto: "))
        price = float(input("Ingrese el precio del producto: "))
        product = Product(name, cant, price)
        stock.append(product)
        print("Producto agregado exitosamente.")
        input("Presiona Enter para continuar...")
    except ValueError:
        print("Error: Entrada no valida")
        input("Presiona Enter para continuar...")

def show_products():
    if stock:
        for i in stock:
            print(f'Nombre: {i.name}, Cantidad: {i.cant}, Precio: {i.price}')
        
        input("Presiona Enter para continuar...")
    else:
        print("No hay productos para mostrar.")
        input("Presiona Enter para continuar...")    

def found_product():
    name = input("Ingrese el nombre del producto que desea buscar: ")
    exist = False
    
    for i in stock:
        if i.name == name:
            print(f'Nombre: {i.name}, Cantidad: {i.cant}, Precio: {i.price}')
            exist = True
            input("Presiona Enter para continuar...")
            break
    if not exist:
        print("Producto no encontrado.")
        input("Presiona Enter para continuar...")
    
def update_product_cant():
    name = input("Ingrese el nombre del producto al que desea actualizar la cantidad: ")
    exist = False
    
    for i in stock:
        if i.name == name:
            print("Información actual del inventario")
            print(f'Nombre: {i.name}, Cantidad: {i.cant}, Precio: {i.price}')
            try:
                i.cant = int(input("Ingresa la cantidad del producto: "))
                print("Información luego de actualizar la cantidad en el inventario")
                print(f'Nombre: {i.name}, Cantidad: {i.cant}, Precio: {i.price}')
                input("Presiona Enter para continuar...")
            except ValueError:
                print("Error: Entrada no valida")
                input("Presiona Enter para continuar...")
            exist = True
            break
    if not exist:
        print("Producto no encontrado.")
        input("Presiona Enter para continuar...")
        
def remove_product():
    name = input("Ingrese el nombre que desea eliminar: ")
    for i in stock:
        if i.name == name:
            stock.remove(i)
            print("Producto eliminado")
            exist = True
            input("Presiona Enter para continuar...")
            break
    if not exist:
        print("Producto no encontrado.")
        input("Presiona Enter para continuar...")
           
while True:
    show_menu()    
    option = input("Elige una opción del menu ")
           
    match option:
        case "1":
            add_product()
        case "2":
            show_products()
        case "3":
            found_product()
        case "4":
            update_product_cant()
        case "5":
            remove_product()
        case "6":
            print("Ha salido del programa.")
            break
        case _:
            print("Opción no válida. Intente nuevamente.")