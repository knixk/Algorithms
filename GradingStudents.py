grade               #in progress
for i in grade:   
    if i >= 38:
        if i % 5 == 3:
            i += 2
        elif i % 5 == 4:
            i += 1
    print (i)
