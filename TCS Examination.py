r = int(input())
while(r):
    a1, s1, d1 = map(int, input().split())
    a2, s2, d2 = map(int, input().split())
    f1 = a1 + s1 + d1
    f2 = a2 + s2 + d2
    if(f1 > f2):
        print("DRAGON")
    elif(f1 < f2):
        print("SLOTH")
    else:
        if(a1 > a2):
            print("DRAGON")
        elif(a1 < a2):
            print("SLOTH")
        else:
            if(s1 > s2):
                print("DRAGON")
            elif(s1 < s2):
                print("SLOTH")
            else:
                print("TIE")
    r -= 1
