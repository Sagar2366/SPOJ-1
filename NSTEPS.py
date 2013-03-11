t=int(raw_input())
while(t>0):
    m,n=map(int,raw_input().split())
    if m==n:
        if m%2==0:
            print 2*m
        else:
            print 2*m-1
    else:
        if n==m-2:
            if m%2==0:
                print m+n
            else:
                print m+n-1
        else:
            print 'No Number'

    t-=1
