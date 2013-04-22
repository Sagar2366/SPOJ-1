def last(a,b):
    if b<=4:
        num=str(pow(a,b))
        return num[-1]
    else:
        if b%4:
            return last(a,b%4)
        else:
            return last(a,4)
t=int(raw_input())
while t:
    t-=1
    a,b = map(int,raw_input().split())
    if b<=4:
        print str(pow(a,b))[-1]
    else:
        if b%4:
            print str(pow(a,b%4))[-1]
        else:
            print str(pow(a,4))[-1]
