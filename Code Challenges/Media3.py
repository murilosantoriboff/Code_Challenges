vals  = input().split()

v1 = float(vals[0])
v2 = float(vals[1])
v3 = float(vals[2])
v4 = float(vals[3])

media = (v1*2 + v2*3 + v3*4 + v4) / (10)

if media >= 7.0:
    print(f'Media: {media:.1f}')
    print('Aluno aprovado.')
elif media >= 5.0 and media <= 6.9:
    v5 = float(input())
    n_media = (media + v5) / 2
    print(f'Media: {media:.1f}')
    print('Aluno em exame.')
    print(f'Nota do exame: {v5:.1f}')
    if n_media >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {n_media:.1f}')
else:
    print(f'Media: {media:.1f}')
    print('Aluno reprovado.')