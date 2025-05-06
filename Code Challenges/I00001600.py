#Faça um algoritmo que leia 10 números e escreva ao final o maior e o menor deles.

maior = 0
menor = 0
for c in range(1,11):
    n = int(input("Escreva um numero: "))
    menor = n
    if n >= maior:
        maior = n
    if n <= menor:
        menor=n

print(maior, menor)