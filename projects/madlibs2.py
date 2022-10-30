# madLibs2.py

print("Welcome to my game! Let's play!")
A1 = "yes"

while A1 == "yes":
    color = input("\nEnter a color: ")
    pluralNoun = input("Enter a plural noun: ")
    celebrity = input("Enter a celebrity: ")

    print("\nRoses are", color)
    print(pluralNoun + " are blue")
    print("I love", celebrity)

    Question = input("\nWant to play again? (yes/no) ").lower()

    if Question == A1:
        print("\nLet's Go")
    else:
        print("Thanks for playing!")
        break

    color1 = input("\nEnter a color: ")
    singNoun = input("Enter a noun: ")
    food = input("Enter a food: ")

    print("\nDogs are", color)
    print("A " + singNoun + " is loud")
    print("I love", food)

    Question = input("\nWant to play again? (yes/no) ").lower()

    if Question == A1:
        print("\nLet's Go")
    else:
        print("Thanks for playing!")
        break
