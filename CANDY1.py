while True:
    n=int(raw_input())
    if n is -1:
        break
    sum=0
    array=[]
    output=0
    for i in range(0,n):      
        i=int(raw_input())
        array.append(i)
        sum+=i
    if sum%n:
        print -1
    else:
        average = sum/n
        for i in array:
            temp=average-i
            if temp>0:
                output+=temp
        print output
