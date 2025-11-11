# funcao_calculadora.py

def calculadora(numero1, numero2, operacao):
    if operacao == "+":
        return numero1 + numero2
    elif operacao == "-":
        return numero1 - numero2
    elif operacao == "*":
        return numero1 * numero2
    elif operacao == "/":
        if numero2 != 0:
            return numero1 / numero2
        else:
            return "Erro: Não é possível dividir um número por 0"
    else:
        return "Operação inválida!"


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
op = input("Digite a operação (+, -, *, /): ")

resultado = calculadora(num1, num2, op)
print(f"O resultado é: {resultado}")
