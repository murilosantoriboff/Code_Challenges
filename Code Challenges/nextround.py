
'''
Logica do problema:

Precisamos pedir o n (numero de participantes) eo k (pontuacao [k-th] ), e as pontuações (pont -> lista)
Iremos verificar se a pontuacao  é maior ou igual e desa maneira iremos passar o candidato.

'''

n, k = map(int, input().split())
pont = list(map(int, input().split()))
res = 0
for c in range(0,n):
	if pont[k-1] == 0 and pont[c] == pont[k-1]:
		res += 0
	elif pont[k-1] <= pont[c]:
		res += 1
	
print(res)
