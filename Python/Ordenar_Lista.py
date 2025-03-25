"""4) Escreva um programa que ordene uma lista numérica com três elementos."""

#Recebe o valor de itens para inserir na lista.
dados = int(input("Quantos dados vão ser inseridos na lista?"))

#Recebe o dado e insere na lista.
Lista = []
for i in range(dados):
    Lista.append(input(f"Digite o {i + 1} item a ser inserido na lista: "))

#Devolve a lista em ordem
print(sorted(Lista))