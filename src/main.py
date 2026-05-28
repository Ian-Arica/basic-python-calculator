# CALCULADORA MEJORADA EN PYTHON

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


def mostrar_menu():
    print("\n========= CALCULADORA =========")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("================================")


def obtener_numeros():
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            return num1, num2
        except ValueError:
            print("Error: Debe ingresar números válidos.")


def main():

    print("Bienvenido a la Calculadora Básica en Python")

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '5':
            print("Gracias por usar la calculadora.")
            break

        if opcion in ['1', '2', '3', '4']:

            num1, num2 = obtener_numeros()

            if opcion == '1':
                resultado = sumar(num1, num2)
                print(f"\nResultado: {num1} + {num2} = {resultado}")

            elif opcion == '2':
                resultado = restar(num1, num2)
                print(f"\nResultado: {num1} - {num2} = {resultado}")

            elif opcion == '3':
                resultado = multiplicar(num1, num2)
                print(f"\nResultado: {num1} × {num2} = {resultado}")

            elif opcion == '4':
                resultado = dividir(num1, num2)
                print(f"\nResultado: {num1} ÷ {num2} = {resultado}")

        else:
            print("Opción inválida. Intente nuevamente.")


# Ejecutar programa
if __name__ == "__main__":
    main()
    