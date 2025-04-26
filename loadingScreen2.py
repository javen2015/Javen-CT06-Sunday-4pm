import time
stars=10
num=2
spaces=7
for i in range(10):
    for i in range(stars):
        print(' '* (stars - i), '*' * num)
        num=num+2
        spaces=spaces+1
        time.sleep(0.01)
    for i in range(stars):
        print(' '* (stars + i), '*' * num)
        num=num-2
        spaces=spaces-1
        time.sleep(0.01)