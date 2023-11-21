import math

def suma_n_numeros():
    numeros = [float(x) for x in input("Ingrese los números separados por espacio: ").split()]
    suma = sum(numeros)
    print("La suma de los números es:", suma)

def producto_n_numeros():
    numeros = [float(x) for x in input("Ingrese los números separados por espacio: ").split()]
    producto = 1
    for num in numeros:
        producto *= num
    print("El producto de los números es:", producto)

def division_entre_dos_numeros():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número (distinto de cero): "))
    if num2 != 0:
        resultado = num1 / num2
        print("La división es:", resultado)
    else:
        print("Error: No se puede dividir por cero.")

def calcular_factorial():
    n = int(input("Ingrese un número para calcular el factorial: "))
    factorial = math.factorial(n)
    print(f"El factorial de {n} es:", factorial)

def imprimir_tablas_multiplicar():
    numero = int(input("Ingrese el número para la tabla de multiplicar: "))
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def calcular_cuadrado_y_cubo():
    numero = float(input("Ingrese un número para calcular su cuadrado y cubo: "))
    cuadrado = numero ** 2
    cubo = numero ** 3
    print(f"El cuadrado de {numero} es: {cuadrado}")
    print(f"El cubo de {numero} es: {cubo}")

def determinar_promedio():
    numeros = []
    while True:
        num = float(input("Ingrese un número (-1 para terminar): "))
        if num == -1:
            break
        numeros.append(num)

    if numeros:
        promedio = sum(numeros) / len(numeros)
        print("El promedio de los números es:", promedio)
    else:
        print("No se ingresaron números para calcular el promedio.")

def valores_maximo_y_minimo():
    n = int(input("Ingrese la cantidad de números enteros que desea introducir: "))
    if n > 0:
        numeros = [int(input(f"Ingrese el número {i + 1}: ")) for i in range(n)]
        maximo = max(numeros)
        minimo = min(numeros)
        print(f"El valor máximo es: {maximo}")
        print(f"El valor mínimo es: {minimo}")
        print(f"Total de valores introducidos: {len(numeros)}")
    else:
        print("Por favor, ingrese una cantidad válida de números.")

# Menú principal
while True:
    print("\nMenú de opciones:")
    print("1. Suma de 'n' números")
    print("2. Producto entre 'n' números")
    print("3. División entre 2 números")
    print("4. Calcular factorial")
    print("5. Imprimir tablas de multiplicar")
    print("6. Calcular cuadrado y cubo de un número")
    print("7. Determinar promedio de una serie de números")
    print("8. Valores máximo y mínimo")
    print("9. Salir")

    opcion = int(input("Seleccione una opción (1-9): "))

    if opcion == 1:
        suma_n_numeros()
    elif opcion == 2:
        producto_n_numeros()
    elif opcion == 3:
        division_entre_dos_numeros()
    elif opcion == 4:
        calcular_factorial()
    elif opcion == 5:
        imprimir_tablas_multiplicar()
    elif opcion == 6:
        calcular_cuadrado_y_cubo()
    elif opcion == 7:
        determinar_promedio()
    elif opcion == 8:
        valores_maximo_y_minimo()
    elif opcion == 9:
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")
