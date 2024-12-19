def fun(n):
    s=0
    while n!=0:
        r=n%10
        n=n//10
        s=s+r
    if s<=9:
        print(s)
    else:
        fun(s)
n=int(input())
fun(n)
