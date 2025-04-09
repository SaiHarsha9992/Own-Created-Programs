r = int(input())
while(r):
    a, s, d, f = map(int, input().split())
    if(d >= a and (s + f) >= a):
        print("YES")
    else:
        print("NO")
    r -= 1
