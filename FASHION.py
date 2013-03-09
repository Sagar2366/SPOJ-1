test = int(raw_input())
while test>0:
    test-=1
    n=int(raw_input())
    guy=sorted(map(int,raw_input().split()))[::-1]
    girl=sorted(map(int,raw_input().split()))[::-1]
    sum = 0
    for i in range(0,n):
        sum+= guy[i]*girl[i]
    print sum
    
