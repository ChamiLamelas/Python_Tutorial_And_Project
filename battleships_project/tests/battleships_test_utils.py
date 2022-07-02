def ships_eq(x,y):
    if len(x) != len(y):
        return False
    
    for i in range(len(x)):
        if x[i] != y[i]:
            return False
    return True

def board_eq(x,y):
    if len(x) != len(y):
        return False
    for i in range(len(x)):
        if len(x[i]) != len(y[i]):
            return False
        for j in range(len(x[i])):
            if x[i][j] != y[i][j]:
                return False
    return True

def trim_newlines(s):
    i = 0
    while i < len(s) and s[i] == '\n':
        i += 1
    j = len(s) - 1
    while j >= 0 and s[j] == '\n':
        j -= 1
    return s[i:j+1]

def check_strs(ls, s):
    start = 0
    for e in ls:
        idx = s.find(e,start)
        if idx == -1:
            return False
        start = idx + len(e)
    return True


