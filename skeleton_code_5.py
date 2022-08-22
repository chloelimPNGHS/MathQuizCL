# This is my skeleton code

# This component asks user if they want to continue playing
def do_you_continue():
    while True:
        want_to_continue = input("Continue? ")

        # Continues code if answer is "yes"
        if want_to_continue == "yes" or want_to_continue == "y" or want_to_continue == "YES" or want_to_continue == "yeS":
            print("sends user to quiz")
            break

        # sends user back to start if answered with "no"
        elif want_to_continue == "no" or want_to_continue == "n" or want_to_continue == "NO" or want_to_continue == "nO":
            print()
            print("Thanks for playing.")
            break

        # sends user back to continue? question if input is invalid
        else:
            print("ERROR: Please type yes or no")


# This is component 2
def instructions():
    while True:
        have_not_played = input("Would you like to see the instructions? ")

        # Prints instructions when have_not_played is answered with "yes"
        if have_not_played == "yes" or have_not_played == "y" or have_not_played == "YES" or have_not_played == "yeS":
            print("**********************************")
            print()
            print("Hello! Welcome to my maths quiz.")
            print("This quiz is intended for students to practise their basic addition and multiplication with.")
            print("The questions will be made of randomly generated numbers from 0 up until 12 and multiplication/addition questions are randomised!")
            print("20 questions will be asked and you will not be timed, but a score of correct answers will be kept.")
            print("Type in your answer next to the question and press 'enter' or 'return' when you're done. Please have fun.")
            print()
            print("**********************************")
            print()
            do_you_continue()
            break

        # sends user to quiz when have_not_played is answered with "no"
        elif have_not_played == "no" or have_not_played == "n" or have_not_played == "NO" or have_not_played == "nO":
            print("sends user to quiz.")
            break

        # sends user back to have_not_played question if input is invalid
        else:
            print("ERROR: Please type yes or no")


# ********************************************************************************************************


# This is component 1
while True:
    played_before = input("Have you played this quiz before? ")

    # Sends user to quiz if played_before is answered with "yes"
    if played_before == "yes" or played_before == "y" or played_before == "YES" or played_before == "yeS":
        print("send user to quiz")
        break

    # sends user to component 2 if played_before is answered with "no"
    elif played_before == "no" or played_before == "n" or played_before == "NO" or played_before == "nO":
        instructions()
        break

    # sends user back to played_before question if input is invalid
    else:
        print("ERROR: Please type yes or no")


# random equation/number generator that has a range of times tables from 0 to 12 component

# number checker - will not crash if user inputs invalid data

# asking equation range - set it so the program can only ask user 20 equations before ending

# possible point system component?

# "do you want to try again?" component
