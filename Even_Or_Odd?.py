
while True:
    try:
        number = int(input("Whats the number you want to check?: "))
        if number % 2 == 0:
            print(f"{number} That's an even number! Have another?")
        else:
            print(f"{number} That's an odd number! Have another?")

    except ValueError:
        print('Please enter a number')
