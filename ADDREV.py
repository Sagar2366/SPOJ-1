N=int(raw_input())
for i in range(0,N):
    a,b=raw_input().split()
    rev_a=''
    rev_b=''
    for j in range(0,len(a)):
        rev_a += a[-1]
        a=a[:-1]
    for j in range(0,len(b)):
        rev_b += b[-1]
        b=b[:-1]
    sum= str(int(rev_a) + int(rev_b))
    for j in range(0,len(sum)):
        b +=sum[-1]
        sum=sum[:-1] 
    i=int(b)
    print i
                   
        
    

    

