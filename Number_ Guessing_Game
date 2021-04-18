import random


def start_game():
    random_number = int(random.randint(1, 10))
    player_name = input("Whats your name?: ")
    answer = input(f"Hi, {player_name.capitalize()} nice to meet wanna play the game? (Enter Yes / No): ")
    attempts = 0

    while answer.lower() == "yes":
        try:

            guess = input("Please write a number between 1 - 10: ")
            if (int(guess) < 1) or (int(guess) > 10):
                print("stay between 1 - 10")

            if int(guess) == random_number:
                print("WOooOw you found the right number")
                attempts += 1
                print(f"You got it with {attempts} attempts")

                play_again = input("Wanna play again? (Enter Yes / No): ")
                if play_again.lower() != "yes":
                    input("Wanna play again? (Enter Yes / No): ")

                if play_again.lower() == "yes":
                    print("Nice Lets Continue")
                    attempts += 0
                    random_number = int(random.randint(1, 10))

                if play_again.lower() == "no":
                    print("Thank you for playing")
                    break

            elif (int(guess) > random_number) and (int(guess) <= 10):
                print("Lower")
                attempts += 1

            elif (int(guess) < random_number) and (int(guess) <= 10):
                print("Higher")
                attempts += 1

        except ValueError as err:
            print("Oh no!, that is not a valid value.")
            print(f"{err}")
    else:
        print("Okay see you! <3")


if __name__ == '__main__':
    start_game()
