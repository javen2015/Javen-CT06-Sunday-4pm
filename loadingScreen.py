for i in range(10000):
    stars=10
    spaces=0
    num=0
    for i in range(stars):
        num=num+2
        spaces=spaces+1
        print(' '* (stars - i), '*' * num)
    stars=0
    for i in range(stars):
        num=num-2
        spaces=spaces-1
        print(' '* (stars - i), '*' * num)