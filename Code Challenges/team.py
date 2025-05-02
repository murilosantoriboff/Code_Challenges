n = int(input())
r = 0

for c in range(0,n):
    a = input()
    if a.count('1') >= 2:
        r += 1

print(r)
