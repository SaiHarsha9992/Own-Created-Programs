for j in range(int(input())):
    n = input()
    a1 = sum(list(map(int, input().split())))
    d1 = sum(list(map(int, input().split())))
    a2 = sum(list(map(int, input().split())))
    d2 = sum(list(map(int, input().split())))
    if a1 > a2 and d1 > d2: print('A')
    elif a1 < a2 and d1 < d2: print('P')
    else: print('DRAW')
