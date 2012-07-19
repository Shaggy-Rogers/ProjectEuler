
def one():
    x = 0
    answer = 0
    while x < 1000:
        if x < 1000:
            if x % 15 == 0 or x % 3 == 0 or x % 5 == 0:
                answer += x
                x += 1
            else:
                x += 1
    print(answer)