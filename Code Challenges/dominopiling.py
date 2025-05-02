'''
    Fazer a logica no final multiplicar e dividir (m*n)//2 ex:

    print(m*n)//2
    


mn = list(input())
if len(mn) == 3:
    a = int(mn[0])
    b = int(mn[2])
    print((a*b)//2)
elif len(mn) > 3:
    pass

a = int(mn[])
b = int(mn[])
print((a*b)//2)
'''
m, n = map(int, input().split())
total = int(m*n / 2)
print(total)
