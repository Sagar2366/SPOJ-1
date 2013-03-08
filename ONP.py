t=int(raw_input())
while(t>0):
    infix=list(raw_input())
    stack=[]
    output=''
    for i in infix:
        if i=='(' or i=='+' or i=='-' or i=='*' or i=='/' or i=='^':
            stack.append(i)            
        elif i==')':
            while(stack[-1]!='('):
                last=stack.pop()
                if last!='(':
                    output+=last
            stack.pop()
        else:
            output+=i
    print output
    t-=1
