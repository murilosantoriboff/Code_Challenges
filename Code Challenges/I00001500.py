# Faça um algoritmo que leia 10 números, positivos ou negativos, e escreva ao final o maior deles

maior = 0
for c in range(1,11):
    n = int(input("Escreva um numero: "))
    if n >= maior:
        maior = n

print(maior)