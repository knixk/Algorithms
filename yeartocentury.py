#A simple program that converts years e.g - 3032 into century i.e - 31

n = int(input())

def year(n):
    n = (n / 100) + 1
    return int(n)
    
print(year(n))
