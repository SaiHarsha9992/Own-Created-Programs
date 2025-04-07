r = int(input())
while(r):
    a = int(input())
    s = input()
    d = 0
    f = 0
    for i in s:
        if(i != 'A' and i != 'E' and i != 'I' and i != 'O' and i != 'U' and i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u'):
            d += 1
            if(d == 4):
                f = 1
                print("NO")
                break
        else:
            d = 0
    if(f == 0):
        print("YES")
    r -= 1
