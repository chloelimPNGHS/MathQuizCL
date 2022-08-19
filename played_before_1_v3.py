# This is component 1
while True:
    played_before = input("Have you played this quiz before? ")

    # Sends user to quiz if played_before is answered with "yes"
    if played_before == "yes" or played_before == "y" or played_before == "YES" or played_before == "yeS":
        print("send user to quiz")
        break

    # sends user to component 2 if played_before is answered with "no"
    elif played_before == "no" or played_before == "n" or played_before == "NO" or played_before == "nO":
            print('have_not_played')
            break

    # sends user back to played_before question if input is invalid
    else:
        print("Please type yes or no")


''' This is a separating line for neatness '''


# This will be component 2
