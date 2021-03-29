def timeConversion(s):
    AM_PM = s[-2:]                                            #[-2:] means the last two numbers
    s = s[:8]
    hh, mm, ss = [int(x) for x in s.split(":")]               #splitting the array and letting the vals be called hh, mm & ss.
                                        
    if AM_PM == 'PM' and hh != 12:                          
        return('{:02}:{:02}:{:02}'.format(hh+12, mm, ss))     #if its pm and hour not set to 12 we set it. 
    elif AM_PM == 'AM' and hh == 12:                          #if its am and hour not set to 00 we set it.
        return('{:02}:{:02}:{:02}'.format(0, mm, ss))         
    else:                                                         
        return('{:02}:{:02}:{:02}'.format(hh, mm, ss))        #finally we return the list
