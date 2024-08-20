def sum(a, b):
    return a + b

def rest(a, b):
    return a - b

def multiply(a, b):
    return a * b

def div(a, b):
    return a / b if b != 0 else "Error: División por cero"

# Función principal de la calculadora
def calculadora():
    while True:
        # Mostramos el menú de opciones
        print("\nCalculadora Básica CalcuMath")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        
        # Solicitamos al usuario que elija una operación
        opcion = input("Elige una operación (número 1 al 5): ")
        
        # Verificamos si el usuario quiere salir
        if opcion == '5':
            print("Saliste de CalcuMath. ¡Vuelve Pronto!")
            break
        
        # Verificamos si la opción es válida
        if opcion not in ['1', '2', '3', '4']:
            print("Opción no válida. Por favor, intenta de nuevo.")
            input("Presiona Enter para continuar...")
            continue
        
        # Pedimos los dos números para realizar la operación
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Error: Por favor, ingresa números válidos.")
            input("Presiona Enter para continuar...")
            continue
        
        # Realizamos la operación según la opción elegida usando match-case
        match opcion:
            case '1':
                print(f'{num1} + {num2} = {sum(num1, num2)}')
            case '2':
                print(f'{num1} - {num2} = {rest(num1, num2)}')
            case '3':
                print(f'{num1} * {num2} = {multiply(num1, num2)}')
            case '4':
                print(f'{num1} / {num2} = {div(num1, num2)}')
        
        # Esperar a que el usuario presione Enter antes de volver al menú
        input("Presiona Enter para continuar...")

# Iniciamos la calculadora
calculadora()