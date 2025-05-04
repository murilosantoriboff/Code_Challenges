"""Dois números n1 e n2 são ditos amigos entre si se a soma dos divisores de n1 (excluindo o próprio
n1) é igual a n2, e a soma dos divisores de n2 (excluindo o próprio n2) é igual a n1. Ex: 220 e 284. Faça um
algoritmo que leia 2 valores e verifique se são amigos entre si escrevendo: 1 - se são amigos; 0 - se não são
amigos."""
div_n1 = list()
div_n2 = list()

n1 = int(input("Digite n1: "))
n2 = int(input("Digite n2: "))

for i in range(1,n1+1):
    if n1 % i == 0:
        div_n1.append(i)

for i in range(1,n2+1):
    if n2 % i == 0:
        div_n2.append(i)

if sum(div_n1) == n2 and sum(div_n2) == n1:
    print("1")

else:
    print("0")