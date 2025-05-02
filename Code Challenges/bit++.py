'''
n -> numeros de operações que irão ser executadas
fazer um for no numero de operações e verificar se existe '++' ou '--'
assim somando 1 ou tirando 1 como o problema pede
'''

n_op = int(input())
x = 0
for cont in range(1, n_op+1):
    op = input()
    if '++' in op:
        x += 1
    elif '--' in op:
        x -= 1
print(x)
