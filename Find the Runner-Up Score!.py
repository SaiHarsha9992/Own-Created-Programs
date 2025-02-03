if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    a=set(arr)
    arr=list(a)
    arr.sort()
    print(arr[-2])
