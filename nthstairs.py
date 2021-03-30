# Solution 1
N = int(10)

def steps(N):
    lst=[0,1,2]                           
    for i in range (3,N+1):
       sum=lst[i-1]+lst[i-2]
       lst.append(sum)
    return lst[N]

print(steps(N))

#Solution 2 


n = int(input())

def climb(n):
    x = int(1)
    y = int(2)
    tmp = int(0)

    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2

    for i in range(3, n+1):
        tmp = y
        y += x
        x = tmp
    return y

print(climb(n))
    
