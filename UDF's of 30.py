#!/usr/bin/env python
# coding: utf-8

# # 1.1

# In[1]:


def fun():
    print("Hello World!")
fun()


# # 1.2

# In[2]:


def fun():
    print("We Aliens Welcome You Human to Our Planet MARS. Prepare to Die!!!")
fun()


# # 1.3

# In[3]:


def fun(n,c,d):
    print(f"{n} from {c}, {d}")
n=input()
c=input()
d=input()
fun(n,c,d)


# # 1.4

# In[4]:


def fun(a,b,c):
    print(a*c+b)
a,b,c=map(int,input().split())
fun(a,b,c)


# # 1.5

# In[5]:


def fun(a,b):
    for i in range(a,b+1):
        print(i,end=' ')
a,b=map(int,input().split())
fun(a,b)


# # 1.6

# In[7]:


def fun(n,r):
    for i in range(1,r+1):
        print(f"{n} x {i} = {n*i}")
n,r=map(int,input().split())
fun(n,r)


# # 1.7

# In[8]:


def fun(a,b,c):
    for i in range(a,b+1,c):
        print(i,end=' ')
a,b,c=map(int,input().split())
fun(a,b,c)


# # 1.8

# In[9]:


def fun(n):
    if n>=90:
        print("O")
    elif n>=80:
        print("A")
    elif n>=70:
        print("B")
    elif n>=60:
        print("C")
    elif n>=50:
        print("D")
    elif n>=35:
        print("E")
    else:
        print("F")
n=float(input())
fun(n)


# # 1.9

# In[12]:


def fun(s,n):
    for i in s:
        if ord(i)<n:
            print(i,end=' ')
s=input()
n=int(input())
fun(s,n)


# # 1.10

# In[14]:


def fun(n,s):
    for i in range(n):
        print(s)
n=int(input())
s=input()
fun(n,s)


# # 1.11

# In[16]:


def fun(n,s1,s2,s3,s4,s5):
    t=s1+s2+s3+s4+s5
    p=t/5
    print(f"{n}'s Total marks = {t} and Percentage = {p}")
n=input()
a,b,c,d,e=map(int,input().split())
fun(n,a,b,c,d,e)


# # 1.12

# In[17]:


def fun(start,stop,num1,num2):
    for i in range(start,stop+1):
        if i%num1==0 and i%num2!=0:
            print(i,end=' ')
st,sp,a,b=map(int,input().split())
fun(st,sp,a,b)


# # 1.13

# In[19]:


def fun(a,b,c):
    print(ord(maxi(a))+ord(mini(a)))
    print(ord(maxi(b))+ord(mini(b)))
    print(ord(maxi(c))+ord(mini(c)))
def maxi(s):
    return max(s)
def mini(s):
    return min(s)
a,b,c=map(str,input().split())
fun(a,b,c)


# # 1.14

# In[21]:


def fun(a,b):
    if a%b==0:
        print("YES")
    else:
        print("NO")
a,b=map(int,input().split())
fun(a,b)


# # 1.15

# In[22]:


def fun(a,b,c):
    return a+b+c
a,b,c=map(int,input().split())
print(fun(a,b,c))


# # 1.16

# In[23]:


def fun(p,t,r):
    s=p*t*r/100
    return s
p,t,r=map(int,input().split())
print(fun(p,t,r))


# # 1.17

# In[25]:


def fun(n,i):
    return n%i==0
n,i=map(int,input().split())
print(fun(n,i))


# # 1.18

# In[29]:


def fun(a,b,c):
    if c==1:
        return a+b
    elif c==2:
        return abs(a-b)
    elif c==3:
        return a*b
    else:
        x="Invalid Choice"
        return x
a,b,c=map(int,input().split())
print(fun(a,b,c))


# # 1.19

# In[33]:


def fun(n):
    c=2
    for i in range(2,n):
        if n%i==0:
            c+=1
    return c
n=int(input())
print(fun(n))


# # 1.20

# In[38]:


def fun(n):
    s=0
    for i in range(1,(n//2)+1):
        if n%i==0:
            s=s+i
    return s
n=int(input())
print(fun(n))


# # 1.21

# In[46]:


def fun(n):
    c=0
    for i in range(2,(n//2)+1):
        if n%i==0:
            c=c+1
    if c==0:
        return True
    else:
        return False
n=int(input())
print(fun(n))


# # 1.22

# In[42]:


def fun(i,r,k):
    c=0
    for i in range(i,r+1):
        if i%k==0:
            c+=1
    return c
i,r,k=map(int,input().split())
print(fun(i,r,k))


# # 1.23

# In[43]:


def fun(n):
    s=0
    while n!=0:
        r=n%10
        n=n//10
        s=s*10+r
    return s
n=int(input())
print(fun(n))


# # 1.24

# In[44]:


def fun(n):
    s=0
    while n!=0:
        r=n%10
        n=n//10
        s=s+r
    return s
n=int(input())
print(fun(n))


# # 1.25

# In[45]:


def fun(n):
    s=1
    while n!=0:
        r=n%10
        n=n//10
        s=s*r
    return s
n=int(input())
print(fun(n))


# # 1.26

# In[49]:


def fun(n,d):
    x=str(n)
    y=str(d)
    if y in x:
        return True
    else:
        return False
n,d=map(int,input().split())
print(fun(n,d))


# # 1.27

# In[52]:


def fun(n,d):
    x=str(n)
    y=str(d)
    c=x.count(y)
    return c
n,d=map(int,input().split())
print(fun(n,d))


# # 1.28

# In[54]:


def fun(n):
    s=0
    x=n
    while n!=0:
        r=n%10
        n=n//10
        s=s*10+r
    return x==s
n=int(input())
print(fun(n))


# # 1.29

# In[58]:


def fun(a,b):
    s=0
    x=a
    while a!=0:
        r=a%10
        a=a//10
        s=s*10+r
    return b==s
a=int(input())
b=int(input())
print(fun(a,b))


# # 1.30

# In[59]:


def fun(s,n):
    x=ord(max(s))
    return x*n
s=input()
n=int(input())
print(fun(s,n))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




