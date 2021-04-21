import random
import string

print('Hello Welcome to Password Generator')


def password_generator():
    try:
        length = int(input('\nEnter the length of password: '))

        where = input('\nPlease enter the name of website trying to create password for it: ')

        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = "-_'."

        clean = lower + upper + num + symbols

        temp = random.sample(clean, length)
        password = ''.join(temp)

        print(f'\nYour password for {where.capitalize()} is {password}')
    except ValueError:
        print('\nPlease Enter a Number')
        return password_generator()


if __name__ == '__main__':
    password_generator()
