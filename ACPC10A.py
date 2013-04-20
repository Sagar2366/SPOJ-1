while(1):
    a,b,c=map(int,raw_input().split())
    if a==b==c==0:
        break
    if b-a==c-b:
        print 'AP', c+b-a
    else:
        print 'GP', c*(b/a)
