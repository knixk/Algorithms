def hurdleRace(k, height):
    
    maxnum = max(height)
    minnum = min(height)
    potions = maxnum - k
    
    if k > maxnum:
        return "0"
    elif k < maxnum:
        return (potions)
    else:
        return "0"
