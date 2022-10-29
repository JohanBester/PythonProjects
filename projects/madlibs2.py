print("Welcome to my game! Let's play!")
A1 = "Yes"

while A1 == "Yes":
    color = input("Enter a color: ")
    pluralNoun = input("Enter a plural noun: ")
    celebrity = input("Enter a celebrity: ")

    print("Roses are", color)
    print(pluralNoun + " are blue")
    print("I love", celebrity)

    Question = input("Want to play again? ")

    if Question == A1:
        print("Let's Go")
    else:
        print("Thanks for playing!")
        Break

    color1 = input("Enter a color: ")
    singnoun = input("Enter a noun: ")
    food = input("Enter a food: ")

    print("Dogs are", color)
    print("A " + singnoun + " is loud")
    print("I love", food)


