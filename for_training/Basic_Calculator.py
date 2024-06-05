def Addition(n1, n2):
    return n1 + n2

def Minus(n1, n2):
    return n1 - n2

def Multiplection(n1, n2):
    return n1 * n2

def Divide(n1, n2):
    return n1 / n2


n1 = int(input('Первое - '))
action = str(input())
n2 = int(input('Второе - '))

if(action == '+'): print(Addition(n1, n2))
if(action == '-'): print(Minus(n1, n2))
if(action == '*'): print(Multiplection(n1, n2))
if(action == '/'): print(Divide(n1, n2))
print('Success!')