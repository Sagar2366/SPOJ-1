def Z(n):
    count=0
    while n>4:
        n//=5
        count+=n
    return count

T=int(raw_input())
while T>0:
    print Z(int(raw_input()))
    T-=1
