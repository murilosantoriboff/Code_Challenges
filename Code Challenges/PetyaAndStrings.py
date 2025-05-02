'''

Logica do problema:

Receberemos a entrada de duas strings de mesmo tamanho, e conferir lexograficamente

'''

res = None
palavra1 = str(input()).lower()
palavra2 = str(input()).lower()

if palavra1 == palavra2:
    res = 0
elif palavra1 < palavra2:
    res = -1
elif palavra1 > palavra2:
    res = 1
print(res)