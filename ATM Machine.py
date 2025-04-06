r = int(input())
while(r):
    a, s = map(int, input().split())
    d = list(map(int, input().split()))
    f = ""
    for i in d:
        if(s >= i):
            s -= i
            f += "1"
        else:
            f += "0"
    print(f)
    r -= 1
