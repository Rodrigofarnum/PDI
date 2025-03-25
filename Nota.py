"""
2) Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.   
"""

#Recebe o valor das notas 1 e 2.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

#Recebe o valor da média
media = (nota1 + nota2) / 2  

#Verifica se o aluno está aprovado ou não.
if media >= 6:
    print("Parabéns, você foi aprovado! Boas férias.")
else:
    print("Você está reprovado. Não desanime e continue tentando! Boas férias.")