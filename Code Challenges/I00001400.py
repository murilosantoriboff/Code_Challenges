# Faça um algoritmo que leia 10 números positivos e escreva ao final o maior deles.

maior = 0
for c in range(1,11):
    n = int(input("Escreva um numero: "))
    if n < 0:
        print("Escreva numeros positivos")
        break
    if n >= maior:
        maior = n

print(maior)