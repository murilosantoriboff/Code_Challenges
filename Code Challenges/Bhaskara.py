vals = input().split()

a = float(vals[0])
b = float(vals[1])
c = float(vals[2])

delta = (b**2) - 4*a*c

while True:

    if a == 0 or delta < 0 :
        print('Impossivel calcular')
        break
    else:
        x1 = (-b + delta ** (1 / 2)) / (2 * a)
        x2 = (-b - delta ** (1 / 2)) / (2 * a)

        print(f'R1 = {x1:.5f}')
        print(f'R2 = {x2:.5f}')
        break