# Calculadora Basica en Python

def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    return num1 / num2

def main():
    print("Bienvenido a la Calculadora Basica en Python")
    print("Seleccione la operación que desea realizar:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = input("Ingrese el número de la operación: ")

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == '1':
        resultado = sumar(num1, num2)
        print(f"El resultado de {num1} + {num2} es: {resultado}")
    elif opcion == '2':
        resultado = restar(num1, num2)
        print(f"El resultado de {num1} - {num2} es: {resultado}")
    elif opcion == '3':
        resultado = multiplicar(num1, num2)
        print(f"El resultado de {num1} * {num2} es: {resultado}")
    elif opcion == '4':
        if num2 != 0:
            resultado = dividir(num1, num2)
            print(f"El resultado de {num1} / {num2} es: {resultado}")
        else:
            print("Error: No se puede dividir por cero.")
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

if __name__ == "__main__":
    main()

