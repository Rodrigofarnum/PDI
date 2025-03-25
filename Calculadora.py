# Recebe os dois números e o sinal da operação
num1 = float(input("Digite o primeiro número: "))
sinal = input("Digite o sinal da operação (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

# Verifica o sinal e executa a operação correspondente
if sinal == "+":
    resultado = num1 + num2
elif sinal == "-":
    resultado = num1 - num2
elif sinal == "*":
    resultado = num1 * num2
elif sinal == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: Divisão por zero não é permitida."
else:
    resultado = "Operação inválida!"

# Exibe o resultado
print(f"O resultado de {num1} {sinal} {num2} é: {resultado}")
