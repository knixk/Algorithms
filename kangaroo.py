def kangaroo(x1, v1, x2, v2):
    if v1 == v2 and x1 == x2:
        return 'YES'
    if v1 == v2 and x1 != x2:
        return 'NO'
    
    nsteps = (x2 - x1) / (v1 - v2):
    if nsteps < 0:
        return 'NO'
    if nsteps == int(steps):
        return 'YES'
    else:
        return 'NO'
