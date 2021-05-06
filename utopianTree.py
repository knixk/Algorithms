#fairly simple problem, we increment when there is a odd number by 1 and multiply by 2 when there is an even.

def utopianTree(n):
    x=0
    for i in range(n+1):
        if i%2:
            x*=2
        else:
            x+=1
    return x
