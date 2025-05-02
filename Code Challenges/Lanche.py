vals = input().split()

val1 = int(vals[0])
val2 = int(vals[1])
tot1 = 0

if val1 == 1:
    print(f'Total: R$ {4.00*val2:.2f}')
elif val1 == 2:
    print(f'Total: R$ {4.50*val2:.2f}')
elif val1 == 3:
    print(f'Total: R$ {5.00*val2:.2f}')
elif val1 == 4:
    print(f'Total: R$ {2.00*val2:.2f}')
elif val1 == 5:
    print(f'Total: R$ {1.50*val2:.2f}')
