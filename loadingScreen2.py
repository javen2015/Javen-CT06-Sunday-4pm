import time
stars=40
num=2
spaces=10
for i in range(100):
    for i in range(stars):
        print(' '* (stars - i), '*' * num)
        num=num+2
        spaces=spaces+1
        time.sleep(0.01)
    num=700
    for i in range(stars):
        print(' '* (stars + i), '*' * num)
        num=num-2
        spaces=spaces-2
        time.sleep(0.01)