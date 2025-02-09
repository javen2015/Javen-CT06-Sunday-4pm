Name = input('Who is the birthday person?')
Age = int(input('How old will he or she be this year?'))
Message = input('What is your personal message to him or her?')

if Age % 10 == 9 :
    print('Happy',Age,'st Birthday,',Name,'!',Message)
elif Age % 10 == 8:
    print('Happy',Age,'nd Birthday,',Name,'!',Message)
    