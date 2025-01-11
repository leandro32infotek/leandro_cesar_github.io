def calculadora():
    operacao = input("Escolha uma operação (+, -, *, /): ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operacao == "+":
        resultado = adicao(num1, num2):
        print("O resultado da adição é:", resultado)
    elif operacao == "-":
        resultado = subtracao(num1, num2):
        print("O resultado da subtração é:", resultado)
    elif operacao == "*":
        resultado = multiplicacao(num1, num2):
        print("O resultado da multiplicação é:", resultado)
    elif operacao == "/":
        resultado = divisao(num1, num2):
        print("O resultado da divisão é:", resultado)
    else:
        print("Operação inválida!")

calculadora()
