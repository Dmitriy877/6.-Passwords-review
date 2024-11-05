enter_password = input('Введите пароль: ')

print('Длина пароля: ', len(enter_password))


for symbol in range(len(enter_password)):
    if enter_password.isdigit() == True:
        print(enter_password[symbol], ' - Число')
    else:
        print(enter_password[symbol], ' - Буква')



if len(enter_password) <= 12:
    print('Короткий')
else:
    print('Длинный')

