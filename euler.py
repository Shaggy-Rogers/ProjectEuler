import check
def one():
    x = 0
    answer = 0
    GIVEN = 1000
    while x < GIVEN:
        if x < GIVEN:
            if x % 15 == 0 or x % 3 == 0 or x % 5 == 0:
                answer += x
                x += 1
            else:
                x += 1
    return(answer)

def two():
    x = 0
    f1 = 1
    f2 = 2
    answer = 2
    GIVEN = 4000000
    while x < GIVEN:
        if x < GIVEN:
            if x % 2 == 0:
                answer += x
                x  = f1 + f2
                f1 = f2
                f2 = x
            else:
                x  = f1 + f2
                f1 = f2
                f2 = x
    return(answer)
    
def three():
    GIVEN = 600851475143  
    x = 0
    y = GIVEN
    z = 0
    answer = 0
    while y != 1:
        while not check.prime(x):
            x += 1
        if check.prime(x):
            if check.whole(y / x):
                y = y / x
                x = 2
                if y != 1:
                    z = y
        x += 1
    answer = z
    return(answer)

def four():
    x = 0
    y = 0
    if check.palendrome(x):
        if y < x:
            y = x 