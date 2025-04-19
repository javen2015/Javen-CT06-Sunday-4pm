while True:
    stars=10
    num=0
    for i in range(Stars):
        num=num+2
        spaces=spaces+1
        print(' '* (Stars - i), '*' * num)