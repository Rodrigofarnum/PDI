"""
3) Escreva um programa que resolva uma equação de segundo grau.   
"""
#É necessário o modulo math para realizar a raiz quadrada do Delta.
import math
#Recebe os valores para a equação.
A = float (input ("Digite o valor de A: "))
B = float (input ("Digite o valor de B: "))
C = float (input ("Digite o valor de C: "))
#Calcula o valor do Delta
Delta = (B * B) - (4*A*C)


#Verifica o valor de x1, x2 e se Delta é negativo.
if Delta < 0:
    print("A equação não possui raizes reais.")
else:
    x1 = (-B + math.sqrt(Delta)) / (2 * A)
    x2 = (-B - math.sqrt(Delta)) / (2 * A)
    print(f"O valor dessa equação é X1 = {x1:.2f} e X2 = {x2:.2f}")
