def balanced_str(p):
    num = 0
    for idx, value in enumerate(p):
        if value == ")":
            num -=1
        if value == "(":
            num +=1
        if num == 0:
            return idx

stack = []
proper_str = ''
def check_proper_str(str):
    for i in range(len(str)):
        if str[i] == '(':
            stack.append(i)
        elif str[i] == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False

def solution(p):
    if p == "" or check_proper_str(p):
        return p
    u, v = p[:balanced_str(p) + 1], p[balanced_str(p) + 1:]
    if check_proper_str(u):
        string = solution(v)
        return u + string
    else:
        t = "("
        t += solution(v)
        t += ")"
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ")"
            elif u[i] == ")":
                u[i] = "("
        t += "".join(u)
        return t

print(solution('(()())()()))(('))