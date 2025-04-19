import time
for i in range(10):
    for i in range(1):
        stars=100
        spaces=100
        num=200
        for i in range(stars):
            print(' '* (stars - i), '*' * num)
            num=num-2
            spaces=spaces-1
            time.sleep(0.01)