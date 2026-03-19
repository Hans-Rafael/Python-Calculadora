def sumar(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Solo se permiten números")
    return a + b


def restar(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Solo se permiten números")
    return a - b


def multiplicar(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Solo se permiten números")
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

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
        return sumar(num1, num2)

    elif operacion == '-':
        return restar(num1, num2)

    elif operacion == '*':
        return multiplicar(num1, num2)

    elif operacion == '/':
        return dividir(num1, num2)

def _validar_numero(a):
    try:
        float(a)
    except ValueError:
        raise ValueError("Debe ingresar un numero valido.")

def _validar_numeros(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Solo se permiten números")

def calculadora():
    print("Calculadora basica: suma, resta, multiplicacion y division")
    
    while True:
        while True:
            num1_str = input("Ingrese el primer numero: ")
            try:
                _validar_numero(num1_str)
                num1 = float(num1_str)
                break
            except ValueError as e:
                print(e)
    
        operacion = pedir_operacion()

        num2 = pedir_numero("Ingrese el segundo numero: ")
        try:
            
            resultado = calcular(num1, num2, operacion)
            print("El resultado es:", resultado)

        except ValueError as e:
            print(e)

        continuar = input("¿Quieres hacer otra operacion? (s/n): ")
        if continuar.lower() != 's':
            break
        
if __name__ == "__main__":
    calculadora()