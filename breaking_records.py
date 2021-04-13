
def breaking_records(scores):
    max = min = score[0]                
    min_count = max_count = 0
    for i in scores:
        if i > max:
            max_count += 1
            max = i
        elif i < min:
            min_count += 1
            min = i
    return max_count, min_count

n = int(input())
scores = list(map(int, input().split()))
print(breaking_records(scores))
