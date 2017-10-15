closer_to_opener = {
    ')': '(',
    ']': '[',
    '}': '{'
}  
 
def is_matched(expression):
    stack = []
    for c in expression:
        if c == '(' or c == '[' or c == '{':
            stack.append(c)
        else:
            if len(stack) and closer_to_opener[c] == stack[-1]:
                stack = stack[:-1]
            else:
                return ['wrong']
    return len(stack) == 0
    


t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
