r = int(input())
while(r):
    a = list(map(int, input().split()))
    a.remove(min(a))
    print(sum(a))
    r -= 1
