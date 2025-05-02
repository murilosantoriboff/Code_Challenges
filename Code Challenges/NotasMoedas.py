val = float(input())

# Declaração das variaveis

notas_100 = 0
notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_5 = 0
notas_2 = 0

moedas_1 = 0
moedas_05 = 0
moedas_025 = 0
moedas_01 = 0
moedas_005 = 0
moedas_001 = 0

# Separação das notas

if val >= 100:
    notas_100 = val // 100
    val -= notas_100*100

if val >= 50:
    notas_50 = val // 50
    val -= notas_50*50

if val >= 20:
    notas_20 = val // 20
    val -= notas_20*20

if val >= 10:
    notas_10 = val // 10
    val -= notas_10*10

if val >= 5:
    notas_5 = val // 5
    val -= notas_5*5

if val >= 2:
    notas_2 = val // 2
    val -= notas_2*2

# Separacao das moedas

if val >= 1:
    moedas_1 = val // 1
    val -= moedas_1*1
print(val)
if val >= 0.50:
    moedas_05 = val // 0.5
    val -= moedas_05*0.5
print(val)
if val >= 0.25:
    moedas_025 = val // 0.25
    val -= moedas_025*0.25
print(val)
if val >= 0.10:
    moedas_01 = val // 0.10
    val -= moedas_01*0.10
print(val)
if val >= 0.05:
    moedas_005 = val // 0.05
    val -= moedas_005*0.05

print(val)

if val >= 0.01:
    moedas_001 = val // 0.01
    val -= moedas_001*0.01

# Mostrando resultado

print(f"""NOTAS:
{int(notas_100)} nota(s) de R$ 100.00
{int(notas_50)} nota(s) de R$ 50.00
{int(notas_20)} nota(s) de R$ 20.00
{int(notas_10)} nota(s) de R$ 10.00
{int(notas_5)} nota(s) de R$ 5.00
{int(notas_2)} nota(s) de R$ 2.00
MOEDAS:
{int(moedas_1)} moeda(s) de R$ 1.00
{int(moedas_05)} moeda(s) de R$ 0.50
{int(moedas_025)} moeda(s) de R$ 0.25
{int(moedas_01)} moeda(s) de R$ 0.10
{int(moedas_005)} moeda(s) de R$ 0.05
{int(moedas_001)} moeda(s) de R$ 0.01""")