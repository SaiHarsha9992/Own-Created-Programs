r = int(input())
while(r):
    a = int(input())
    s = list(map(int, input().split()))
    for i in range(a):
        if(s[i] >= s[a - 1]):
            print(a - i - 1)
            break;
    r -= 1
