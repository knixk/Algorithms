def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(len(ar)):                  # Looping through each character.
        for j in range(i+1, len(ar)):         # Each times for value of i our counter stops and add one for every element.
            if((ar[i]+ar[j]) % k == 0):      
                count += 1
    return count
