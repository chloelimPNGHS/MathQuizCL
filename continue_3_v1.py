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
