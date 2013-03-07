from math import sqrt

boundcap=1000000000
squarecap=int(sqrt(boundcap))+1
masterlist=[False]*2 + [True]*2 + [False,True]*(((squarecap-4)//2)+1)
masterlength=len(masterlist)-1


def sieve():
    i=3
    while (i<=masterlength):        
        if i%6==1 or i%6==5 or i==2 or i==3:            
            if masterlist[i]:
                if i*i<=masterlength:
                    for j in range(i*i,masterlength+1,i):
                        masterlist[j]=False                    
                        
        i+=2
sieve()     

test=int(raw_input())
while test>0:
    m,n=map(int,raw_input().split())
    
    if (n<=masterlength):
        if m%2==0:
            if m==2:
                print m
            for i in range(m+1,n+1,2):
                if i%6==1 or i%6==5 or i==2 or i==3:
                    if masterlist[i]:
                        print i
        else:
            if m==1:
                print m+1
            for i in range(m,n+1,2):
                if i%6==1 or i%6==5 or i==2 or i==3:
                    if masterlist[i]:
                        print i
        
    elif (m>masterlength):
        if m%2==0 and (n-m+1)%2==1:
            current = [False,True]*((n-m+1)//2)+[False]
            
        elif m%2==0 and (n-m+1)%2==0:
            current = [False,True]*((n-m+1)//2)
            
        elif m%2==1 and (n-m+1)%2==1:
            current = [True,False]*((n-m+1)//2)+[True]
            
        elif m%2==1 and (n-m+1)%2==0:
            current = [True,False]*((n-m+1)//2)
    
        for i in range(3,masterlength+1,2):
            if i%6==1 or i%6==5 or i==2 or i==3:
                if masterlist[i]:
                    for j in range( (m//i)*i, n+1,i):
                        if j-m>=0:
                            current[j-m]=False
        for i in range(m,n+1):
            if current[i-m]:
                print i
                
    elif (m<=masterlength and n> masterlength):
        if m%2==0:
            if m==2:
                print m
            for i in range(m+1,masterlength+1,2):
                if i%6==1 or i%6==5 or i==2 or i==3:
                    if masterlist[i]:
                        print i
        else:
            if m==1:
                print m+1
            for i in range(m,masterlength+1,2):
                if i%6==1 or i%6==5 or i==2 or i==3:
                    if masterlist[i]:
                        print i
                        
        if (n-masterlength+1)%2==1:
            current = [True,False]*((n-masterlength+1)//2)+[True]
            
        else:
            current = [True,False]*((n-masterlength+1)//2)
            
        for i in range(3,masterlength+1,2):
            if i%6==1 or i%6==5 or i==2 or i==3:
                if masterlist[i]:
                    for j in range((masterlength//i)*i, n+1,i):
                        if j-masterlength>=0:
                            current[j-masterlength]=False
                            #print j,current[j-m]
                            
        for i in range(masterlength,n+1):
            if current[i-masterlength]:
                print i
    print '\n'
    test-=1
