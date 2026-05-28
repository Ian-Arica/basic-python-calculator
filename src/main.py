# Calculadora Basica en Python

def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:
        return "Error: No se puede dividir por cero."
    return num1 / num2

def main():
    print("=== CALCULADORA PYTHON ===")
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
        print(f"El resultado es: {resultado}")

    elif opcion == '2':
        resultado = restar(num1, num2)
        print(f"El resultado es: {resultado}")

    elif opcion == '3':
        resultado = multiplicar(num1, num2)
        print(f"El resultado es: {resultado}")

    elif opcion == '4':
        resultado = dividir(num1, num2)
        print(f"El resultado es: {resultado}")

    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()