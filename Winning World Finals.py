q = int(input())
for w in range(0, q):
    a, s = list(map(int, input().split()))
    e = (1000 - a - s) // 21
    r = 299 - a
    print(min(e, r))
