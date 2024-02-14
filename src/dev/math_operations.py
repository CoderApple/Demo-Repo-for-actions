def add(a,b):
    s=a+b
    return s

def sub(a,b):
    return a-b

def divide(a,b):
    if b==0:
        raise ZeroDivisionError("Cannot divide by Zero")
    return a/b

def average(n):
    if len(n)!=0:
        total=sum(n)
        avg=total/len(n)
        return avg
    else:
        return 0

def operation(a,b):
    if b==0:
        raise ZeroDivisionError("Cannot divide by Zero")
    d=a/b
    m=a*b
    s=a+b
    sub=a-b
    return (d,m,s,sub)







