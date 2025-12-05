a, s, d = list(map(int, input().split()))
t1 = a + (s * 0.5)
t2 = d + (s * 0.5)
m = a + s + d
t1 = t1 + (4 - m)
if t1 > t2:
    print('YES')
else:
    print("NO")
