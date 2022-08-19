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
