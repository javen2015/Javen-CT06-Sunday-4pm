while True:
    stars=10
    spaces=0
    num=0
    for i in range(stars):
        num=num+2
        spaces=spaces+1
        print(' '* (Stars - i), '*' * num)