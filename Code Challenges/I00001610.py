"""Faça um algoritmo que leia um valor n (n>=1) correspondente ao número de alunos de uma
turma. Após, o algoritmo lê as notas das provas dos n alunos dessa turma. As notas deverão ser lidas até que
sejam informadas n notas válidas, ou seja, no intervalo [0, 10], descartando as notas fora desse intervalo. As
notas somente poderão ser lidas uma única vez. O algoritmo deve informar qual foi a menor nota e o
percentual dos alunos que tiraram a menor nota (que não é, necessariamente, 0). Por exemplo, se o valor lido
para n foi 20 e as notas foram 6.0 6.5 8.0 9.0 4.5 3.0 9.0 8.5 4.5 3.0 6.0 3.0 8.0 9.0 4.5 10 9.0 8.5 4.5 3.0 o
algoritmo escreve 3.0 e 20, já que quatro (20% de 20) alunos tiraram essa nota."""

c_notas = 0
n = int(input("Escreva quantidade de alunos: "))
menor = 11
a = list()
for c in range(1,n+1):
    nota = float(input("Escreva a nota: "))
    if nota <=10 and nota >=0:
        a.append(nota)
        if nota <= menor:
            menor = nota

c_notas = a.count(menor)
print(f"A nota menor é {menor} e foi cerca de {(c_notas*100)/(n)}% entre {n} alunos")