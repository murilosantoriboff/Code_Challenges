conta = input().split('+')

conta.sort()

res = ''

for el in conta:
    res = res + el + '+'

print(res[:-1])