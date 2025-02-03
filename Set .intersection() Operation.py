# Enter your code here. Read input from STDIN. Print output to STDOUT
en=int(input())
e=set(map(int,input().split()))
fn=int(input())
f=set(map(int,input().split()))
x=e.intersection(f)
print(len(x))
