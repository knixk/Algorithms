input()
def migratoryBirds(arr):
    count = [0] * 6               #creates an array of 6 digits
    for i in arr:   
        count[i] += 1
    return count.index(max(count))        #return the index of the max count

arr = map(int, input().split())
print(migratoryBirds(arr))
