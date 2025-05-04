"""Um número inteiro maior do que 1 é primo se ele possui como divisores somente o 1 e ele
mesmo. Faça um algoritmo que leia um número e verifique se é primo escrevendo: 1 - se o número é primo; 0
- se o número não é primo. Dica:Pode-se também verificar se um número é primo encontrando seu primeiro
divisor maior que 1. Se o primeiro divisor for o próprio número, ele é primo."""

n = int(input("Digite um numero e veja se ele é primo: "))

if n <=1:
    print("0")
else:
    for i in range(2,n):
        if n % i == 0:
            print("0")
            break

        else:
            print("1")
            break