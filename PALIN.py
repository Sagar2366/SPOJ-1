def inc(left):
    leftlist=list(left) 
    last = len(left)-1 
    while leftlist[last]=='9': 
        leftlist[last]='0'
        last-=1
    
    leftlist[last] = str(int(leftlist[last])+1)
    return "".join(leftlist)
    
        
def palin(number):
    size=len(number)
    odd=size%2
    if odd:
        center=number[size/2]
    else:
        center=''
    left=number[:size/2]
    right = left[::-1]
    pdrome = left + center + right
    if pdrome > number:
        print pdrome
    else:
        if center:
            if center<'9':
                center = str(int(center)+1)
                print left + center + right
                return
            else:
                center = '0'
        if left == len(left)*'9':
            print '1' + (len(number)-1)*'0' + '1'
        else:
            left = inc(left)
            print left + center + left[::-1]
        
            

test=int(raw_input())
while test>0:
    test-=1
    number=raw_input()
    palin(number)
