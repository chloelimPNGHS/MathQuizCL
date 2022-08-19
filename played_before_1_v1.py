# This is component 1
played_before = input("Have you played this quiz before? ")
have_not_played = input("Would you like to see the instructions? ")

if played_before == "yes" or played_before == "y" or played_before == "YES" or played_before == "yeS":
    print("send user to quiz")

elif played_before == "no" or played_before == "n" or played_before == "NO" or played_before == "nO":
        print(have_not_played)

else:
    print("Please type yes or no")
