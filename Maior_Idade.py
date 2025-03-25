"""
1) Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.   
"""
#Recebe a idade do usuário e verifica se é um número inteiro .
try: 
    idade = int(input("Digite dua idade: "))
except:
    print("Digite um número inteiro.")  
    idade = 0
#Verifica se é maior que 18 anos
if idade >= 18: 
    print("Maior de idade. Pode passar, aproveite!")
else:
    print("Para acessar essa área é necessario ser maior de idade 18+")
