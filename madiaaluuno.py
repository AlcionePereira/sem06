def alunos(a, b, c,):
    n1 = a
    n2 = b
    n3 = c
    med = (a + b + c) / 3
    
    if c > 8:
        return med+1
    else:
        return med


n1 = int(input())
n2 = int(input())
n3 = int(input())

if alunos( n1, n2, n3)  > 10:
    print(f'{10}')

else:
    print(alunos(n1, n2, n3))


    

          

