stack=[]
for i in s:
    if i=="(" or i=="{" or i=="[":
        stack.append(i)
    else:
        if len(stack) == 0 or i==')' and stack[-1]!='(' or i=='}' and stack[-1]!='{' or i==']' and stack[-1]!='[' :
            return False
        else :
            stack.pop()
return len(stack)==0