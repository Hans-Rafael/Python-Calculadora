def pedir_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Debe ingresar un numero valido.")


def pedir_operacion():
    while True:
        operacion = input("Ingrese la operacion (+, -, *, /): ")
        if operacion in ['+', '-', '*', '/']:
            return operacion
        else:
            print("Operacion no valida.")


def calcular(num1, num2, operacion):

    if operacion == '+':
        return num1 + num2
    elif operacion == '-':
        return num1 - num2
    elif operacion == '*':
        return num1 * num2
    elif operacion == '/':
        if num2 == 0:
            raise ValueError("No se puede dividir por cero.")
        return num1 / num2


def calculadora():

    print("Calculadora basica: suma, resta, multiplicacion y division")

    num1 = pedir_numero("Ingrese el primer numero: ")
    operacion = pedir_operacion()

    while True:
        num2 = pedir_numero("Ingrese el segundo numero: ")

        if operacion == '/' and num2 == 0:
            print("No se puede dividir por 0.")
        else:
            break

    resultado = calcular(num1, num2, operacion)

    print("El resultado es:", resultado)


if __name__ == "__main__":
    calculadora()