# Desenvolva uma calculadora simples em Python que realize operações básicas,
# como adição, subtração, multiplicação e divisão.
def calculadora():
    num1 = float(input("Digite o primeiro número: "))
    operador = input("Digite o operador (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))

    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        resultado = num1 / num2
    else:
        print("Operador inválido!")

    print("O resultado é:", resultado)


calculadora()
