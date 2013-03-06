T=int(raw_input())
def f(n):
    if n<2:
        return n
    else:
        return n*f(n-1)
while T>0:
    print f(int(raw_input()))
    T-=1
