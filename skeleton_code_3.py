# ********This is my skeleton code********

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

# ***********************************************************************************************************

# This is component 2
def instructions():
    while True:
        have_not_played = input("Would you like to see the instructions? ")

        # Sends user to instructions when have_not_played is answered with "yes"
        if have_not_played == "yes" or played_before == "y" or played_before == "YES" or played_before == "yeS":
            print("send user to instructions")
            break

        # sends user to quiz when have_not_played is answered with "no"
        elif have_not_played == "no" or played_before == "n" or played_before == "NO" or played_before == "nO":
            print("sends user to quiz")
            break

        # sends user back to have_not_played question if input is invalid
        else:
            print("ERROR: Please type yes or no")

# random equation/number generator that has a range of times tables from 0 to 12 component

# number checker - will not crash if user inputs invalid data

# asking equation range - set it so the program can only ask user 20 equations before ending

# possible point system component?

# "do you want to try again?" component
