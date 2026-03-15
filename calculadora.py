print("Calculadora basica: suma, resta, multiplicacion y division")

# Primer numero
while True:
    try:
        num1 = float(input("Ingrese el primer numero: "))
        break
    except ValueError:
        print("Debe ingresar un numero valido.")

# Operacion
while True:
    operacion = input("Ingrese la operacion (+, -, *, /): ")
    if operacion in ['+', '-', '*', '/']:
        break
    else:
        print("Operacion no valida.")

# Segundo numero
while True:
    try:
        num2 = float(input("Ingrese el segundo numero: "))
        
        if operacion == '/' and num2 == 0:
            print("No se puede dividir por 0.")
        else:
            break
            
    except ValueError:
        print("Debe ingresar un numero valido.")

# Calculo
if operacion == '+':
    resultado = num1 + num2
elif operacion == '-':
    resultado = num1 - num2
elif operacion == '*':
    resultado = num1 * num2
elif operacion == '/':
    resultado = num1 / num2

print("El resultado es:", resultado)

#### Calculador completa con funciones######