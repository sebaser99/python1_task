# num_1 = 4
# num_2 = 6

# result = num_1 + num_2
# result_2 = str(result)
# print("El resultado es: " + result_2)
# print(num_1,  "+", num_2, "=", result_2)

# print("Busqueda")
# mensaje = "Hola Jose"
# buscar_subcadena = mensaje.find("Jose")
# print(buscar_subcadena)

# print("Extracción")
# mensaje = "Hola Jose"
# extraer_cadena = mensaje[1:7]
# print(extraer_cadena)

#ACT1 CONDICIONAL SI
# if condicion_logica
#     instrucciones

# if(True):
#     print("Se ha ingresado a la estructura de control if")
    

# #ACT2 CONDICIONAL SI
# # num1= 5
# # if(num1==5):
# #     print("El número es cinco")
# # print("fin")

# #ACT3
# # a = 4
# # b = 0

# # if b!=0:
# #     print(a / b)

# # #ACT4 Sistema para calcular promedio de notas
# # print("Sistema para calcular promedio de notas de estudiante")
# # name = input("Por favor ingresar nombre")
# # nota1 = int(input(name + "digitar calificación nota 1")) 
# # nota2 = int(input(name + "digitar calificación nota 2")) 
# # nota3 = int(input(name + "digitar calificación nota 3")) 
# # prom = (nota1 + nota2 + nota3) / 3
# # prom = int(prom)
# # if prom >= 3:
# #     print("Hola, " + name + ". Felicitaciones, has aprobado con un promedio de " + str(prom) + ".")
# # print("fin")


# #ACT5 Sentencias condicionales compuestas
# print("Sistema para calcular promedio de notas de estudiante")
# name = input("Por favor ingresar nombre")
# nota1 = int(input(name + "digitar calificación nota 1")) 
# nota2 = int(input(name + "digitar calificación nota 2")) 
# nota3 = int(input(name + "digitar calificación nota 3")) 
# prom = (nota1 + nota2 + nota3) / 3
# prom = int(prom)
# if prom >= 3:
#     print("Hola, " + name + ". Felicitaciones, has aprobado con un promedio de ",prom, ".")
# else:
#     print("Hola, " + name + ".  has REPROBADO con un promedio de " + str(prom) + ".")
# print("fin")

#ACT6
# print("=========================")
# print("Conversor de números")
# print("=========================")

# num1 = int(input("¿Cuál es el número que desea convertir?"))

# if num1 == 1:
#     print("El número es UNO")
# elif num1 == 2:
#     print("El número es DOS")
# elif num1 == 3:
#     print("El número es TRES")
# elif num1 == 4:
#     print("El número es CUATRO")
# elif num1 == 5:
#     print("El número es CINCO")
# else:
#     print("El número no está en la lista")


# #CONVERTIR CADENAS A MINÚSCULAS
# cadena = "La Mejor Cadena"
# print(cadena.lower())

# #CONVERTIR CADENAS A MAYÚSCULAS
# cadena = "La Mejor Cadena"
# print(cadena.upper())

# #CONVERTIR CADENAS A MAYÚSCULAS  Y VICEVERSA
# cadena = "La Mejor Cadena"
# print(cadena.swapcase())

# #CONVERTIR CADENAS A FORMATO TITULO
# cadena = "La Mejor Cadena"
# print(cadena.title())


#ACTIVIDAD 3
# print("=================")
# print("****Conversor****")
# print("=================")
# print("Menú de opciones \n")
# menu= ""
# print("Presiona 1 para convertir de número a palabra \n")
# print("Presiona 2 para convertir de palabra a número \n")

# print(menu)
# opcion = int(input("¿Cuál es la opción deseada?"))
# if opcion == 1:
#     print("\n conversor de número a palabra \n")
#     opcion_uno = int(input("¿Cuál es el número que deseas convertir?"))
#     if opcion_uno == 1:
#         print("El número es uno")
#     elif opcion_uno == 2:
#         print("El número es dos")
#     elif opcion_uno == 3:
#         print("El número es tres")
#     elif opcion_uno == 4:
#         print("El número es cuatro")
#     elif opcion_uno == 5:
#         print("El número es cinco")
#     else: 
#         print("El número no está registrado")
# elif opcion == 2:
#     print("\n conversor de palabra a número \n")
#     opcion_dos = input("¿Cuál es la palabra-número que desea convertir a número?")
#     opcion_dos= opcion_dos.lower()
#     #opcion_dos = int(input("¿Cuál es la palabra-número que desea convertir a número?")-lower())
#     if opcion_dos == "uno":
#         print("El número es ", 1)
#     elif opcion_dos == "dos":
#         print("El número es ", 2)
#     elif opcion_dos == "tres":
#         print("El número es ", 3)
#     elif opcion_dos == "cuatro":
#         print("El número es ", 4)
#     elif opcion_dos == "cinco":
#         print("El número es", 5)
#     else: 
#         print("La palabra-número no está registrada")



#ACTIVIDAD 4
# menu ="""=================
# "****Registro de Usuarios****"
# "================="
# "Bienvenido al registro de usuarios, por favor digitar la opción que desee del 1 al 3 \n"
# "[1] Digitar su Nombre "
# "[2] Digitar su edad "
# "[3] Digitar su correo electrónico "
# """
# print(menu)
# opcion = input("Digite una opción del 1 al 3")
# if opcion == '1':
#     nombre = input("Ingresa tu nombre") 
#     print("Su nombre es " + nombre)
#     print("Su nombre es ", nombre)
#     print(f"Su nombre es {nombre}")
#     print("Su nombre es {}".format(nombre))
# elif opcion == '2':
#     edad = int(input("Ingresa tu edad"))
#     print("Su edad es " + edad)
#     print("Su nombre es ", edad)
#     print(f"Su nombre es {edad}")
#     print("Su nombre es {}".format(edad))
# elif opcion == '3':
#     correo = input("Ingresa tu correo")
#     print("Su correo es " + correo)
#     print("Su correo es ", correo)
#     print(f"Su correo es {correo}")
#     print("Su correo es {}".format(correo))
# else:
#     print("Debes digitar un número entre 1 y 3")
#     print("****" * 20)


#ACTIVIDAD 4
# menu ="""=================
# "****Registro de Usuarios****"
# "================="
# "Bienvenido al registro de usuarios, por favor digitar la opción que desee del 1 al 3 \n"
# "[1] Digitar su Nombre "
# "[2] Digitar su edad "
# "[3] Digitar su correo electrónico "
# """
# print(menu)
# opcion = input("Digite una opción del 1 al 3 \n")
# if opcion == '1':
#     nombre = input("Ingresa tu nombre  ") 
#     if nombre.isalpha(): #cadena str
#         print("Su nombre es " + nombre)
#         print("Su nombre es ", nombre)
#         print(f"Su nombre es {nombre}")
#         print("Su nombre es {}".format(nombre))
#     else: print("Has digitado un nombre que no es válido")
# elif opcion == '2':
#     edad = input("Ingresa tu edad  ")
#     if edad.isnumeric():
#         print("Su edad es " + edad)
#         print("Su nombre es ", edad)
#         print(f"Su nombre es {edad}")
#         print("Su nombre es {}".format(edad))
#     else: print("Has digitado una edad que no es válida")
# elif opcion == '3':
#     correo = input("Ingresa tu correo  ")
#     if correo.find('@')>=0 and correo.find('.')>=0:
#         print("Su correo es " + correo)
#         print("Su correo es ", correo)
#         print(f"Su correo es {correo}")
#         print("Su correo es {}".format(correo))
#     else: print("Has digitado un correo que no es válido")
# else:
#     print("Debes digitar un número entre 1 y 3")
#     print("****" * 20)


#formato

# flor = "rosas"
# print(f'El jardín de mi casa está lleno de {flor!r}')

# modelo = "Optimus Tucan"
# precio = 190000
# impuesto = precio * 19 /100

# print(f'Bicicleta {modelo} tiene un valor de: {precio + impuesto} pesos')


####LISTAS
#list= ["lunes", "martes", "miercoles", "jueves", "viernes"]
#print(lista[3])

#listas y tuplas
# nums=[1,2,3,4,5,6]
# tupla=(10,20,30,40,50)
# print(nums[0])
# print(tupla[2])

# nums[0] = 100
# print(nums[0])

# #agregar 
# nums.append(6)
# print(nums)


##ACTIVIDAD 5
# mi_lista = [1,2,"hola", 3.14]
# print(mi_lista)
# a = [1,3,5,8,9]
# print(a)

# objeto= (7, "hola", True, 3.14)
# print(objeto)

# mi_tupla = (10, 20, 30)
# print(mi_tupla)

# #conjunto de datos .. que se agregan de manera desordenda y no pueden tener info duplicada
# mi_conjunto = {1, 2, 3}
# print(mi_conjunto)

# #conjunto vacio
# primer_conjunto = set()
# primer_conjunto.add(3)
# primer_conjunto.add("hola")
# print(primer_conjunto)
# primer_conjunto.discard("hola")
# print(1 in mi_conjunto)

#diccionarios..tipo de colección de datos donde se puede guardar 
# desordenadamente y guarda dos elementos por posición, clave y valor
# diccionario = {"blue": "azul", "a": "A"}
# print(diccionario["blue"])
# diccionario["uno"] = 1
# print(diccionario)
# # del (diccionario["uno"])
# print(diccionario)

# diccionario = {"Pedro": {"Edad": 22, "Altura": 1.65}, "Ana": [25, 1.70], "Maria": [30, 1.75]}

#CICLO FOR
# nums = [4, 78, 9 , 81]
# for n in nums:
#     print(n)

# for i in range(0,5):
#     print(i)
#     if(i == 2):
#         print("OK")


# for i in range(10, -1, -1):
#     print(i)
#     if(i == 2):
#         print("OK")
   
# x= 0     
# while x < 10:
#     print(x)
#     x += 1
    
# x=0
# while x < 10:
#     print(x)
#     x += 1

#decrementar
# x=9
# while x > 0:
#     print(x)
#     x -= 1

# x = 0
# while x < 100:
#     x += 2
#     print(x)
#     if(x == 100 ):
#         print("El bucle ha finalizado")

x = 20

while x > 0:
    print("Valor de la variable actual ", x)
    x -= 1
    if x ==  7:
        break   
print("Gracias")


def numeroMayor(n1, n2):
    if n1 > n2:
        max = n1
    else:
        max = n2
    return max

print('digitar primer número: ')
n1 = int(input("por favor digitar número 1"))
print("digitar segundo número")    
n2 = int(input("por favor digitar número 2"))
mayor = numeroMayor(n1, n2)
print("El número mayor es ", mayor)