def palendrome(input):
    sinput = "junk"
    sinput = str(input) 
    if sinput == sinput[::-1]:
        return(True)
    return(False)
    
def prime(input):
    if input % 2 != 0 and input % 3 != 0 and input % 5 != 0:
        if input % 7 != 0:
            return(True)
    if input == 2 or input == 3 or input == 5 or input == 7:
        return(True)
    if input == 0:
        return(False)
    return(False)
    
def whole(input):
    if input % 1 != 0:
        return(False)
    return(True)