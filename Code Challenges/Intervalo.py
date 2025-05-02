val = float(input())

if val >= 0 and val <= 25.0000:
    print('Intervalo [0,25]')
elif val > 25.0000 and val <= 50.0000000:
    print('Intervalo (25,50]')
elif val > 50.0000000 and val <= 75.00000:
    print('Intervalo (50,75]')
elif val > 75.000000 and val <= 100:
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')
