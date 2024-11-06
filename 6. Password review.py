# password = input('Введите пароль: ')
#
# print('Длина пароля: ', len(password))
#
#
# for symbol in range(len(password)):
#     if password[symbol].isdigit() == True:
#         print(password[symbol], ' - Число')
#     else:
#         print(password[symbol], ' - Буква')


def has_digit(password):
    number_found = False
    for symbol in range(len(password)):
        if password[symbol].isdigit() == True:
            number_found = True
            return number_found
    return number_found


# if has_digit(password)== True:
#     print("Цифры есть")
# else:
#     print("Цифр нет")


if len(password) <= 12:
    print('Короткий')
else:
    print('Длинный')

print(has_digit("rnfeinginr"))  # False
print(has_digit("rnvnreiv83282"))  # True
