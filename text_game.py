import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


line1 = ("It is the final test for the semester "
         "and this determines your next promotion.")

line2 = ("You are expected to be seated before the invigilator comes in.")

line3 = ("On getting to the class, you find out that your seat "
         "is being occupied by a scary bully.")

randOpt1 = ("You are being sent out for standing."
            "You have failed!")

randOpt2 = ("The Bully is being sent out by the Teacher."
            "You passed the test")


def intro():
    print_pause(line1)
    print_pause(line2)
    print_pause(line3)


def valid_input(prompt, options):
    while True:
        option = input(prompt)
        if option in options:
            return option
        print_pause(f'Sorry, the option "{option}" is invalid. Try again!')


def get_choice(randopt1, randopt2):
    choice = valid_input("What action would you like to take? \n"
                         "1. Leave the class. \n"
                         "2. Fight for you right! \n",
                         ['1', '2'])
    if choice == '1':
        print_pause("You are too weak!")
        print_pause("You failed!")
    else:
        print_pause("You are strong!")
        print_pause("Let's take him down!")
        choice = valid_input("would you like to report to a teacher or "
                             "want to handle him yourself? \n"
                             "1. Report. \n"
                             "2. Handle Him! \n", ["1", "2"])
        if choice == '1':
            result = [randopt1, randopt2]
            print_pause(random.choice(result))
        else:
            result = ["You defeated the bully. \nYou passed the Test!",
                      "The Bully defeated you. \nYou failed the test!"]
            print_pause(random.choice(result))


def play_game():
    while True:
        get_choice(randOpt1, randOpt2)
        break


def play_again():
    choice = valid_input("Would you love to play again? \n"
                         "1. Replay. \n"
                         "2. Exit \n", ["1", "2"])
    if choice == '2':
        print('Thanks for playing! Goodbye!')
        exit(0)
    else:
        print("Let's go there!")


def game():
    intro()
    while True:
        play_game()
        play_again()


if __name__ == '__main__':
    game()
