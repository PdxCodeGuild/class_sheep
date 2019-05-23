
while True:
    continue_playing = input("Would you like to play a game of mad lib? yes or no: ")
    if continue_playing == "no":
        break

    verb = input("Enter a verb ending in \"ing\": ")
    noun = input("Enter a plural noun: ")
    adjective = input("Enter an adjective: ")

    print ("------------------------------------------")
    print(f"\"There are too many {verb} {noun} in this {adjective} car!\" they screamed.")
    print ("------------------------------------------")

