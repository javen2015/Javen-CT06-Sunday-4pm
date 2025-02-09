# Name = input('Who is the birthday person?')
# Age = int(input('How old will he or she be this year?'))
# Message = input('What is your personal message to him or her?')
# if Age == 11 or Age == 12:
#     print('Happy',Age,'th Birthday,',Name,'!',Message)
# elif Age % 10 == 1 :
#     print('Happy',Age,'st Birthday,',Name,'!',Message)
# elif Age % 10 == 2:
#     print('Happy',Age,'nd Birthday,',Name,'!',Message)
# elif Age % 10 == 3:
#     print('Happy',Age,'rd Birthday,',Name,'!',Message)
# else:
#     print('Happy',Age,'th Birthday,',Name,'!',Message)
# for i in range(100):
#         print("I like cake.")
#         print("Give me more.")
# num = 0
# for i in range(0,10,1):
#     num=num+i
#     print(num)
Stars = int(input('How many stars are there?'))
num = 0

for i in range(Stars):
    num=num+1
    space=spaces+1
    print('*' * num)
