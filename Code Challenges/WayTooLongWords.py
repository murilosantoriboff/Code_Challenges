n = int(input())

for p in range(0,n):
    x = str(input()).strip()
    l = len(x)
    if l > 10:
        print(x[0], end='')
        print(l-2, end='')
        print(x[l-1])
    else:
        print(x)
        
    
