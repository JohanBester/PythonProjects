# Case with the traditional if...elif statement

print("\nTraditional case with If...Else:")
age = int(input("Enter your age : "))

if age > 80:
    print("You are too old to party, granny.")
elif age < 0:
    print("You're yet to be born")
elif age >= 18:
    print("You are allowed to party")
else:
    "You're too young to party"


# spoofing a switch case using a def
"""
def switch(lang):
    if lang == "JavaScript":
        return "You can become a web developer."
    elif lang == "PHP":
        return "You can become a backend developer."
    elif lang == "Python":
        return "You can become a Data Scientist"
    elif lang == "Solidity":
        return "You can become a Blockchain developer."
    elif lang == "Java":
        return "You can become a mobile app developer"

print(switch("JavaScript"))
print(switch("PHP"))
print(switch("Java"))
"""

# python 3.10 switch case method

print("\nPython 3.10 Switch Case:")
lang = input("What's the programming language you want to learn? ")

match lang:
    case "JavaScript":
        print("You can become a web developer.")

    case "Python":
        print("You can become a Data Scientist")

    case "PHP":
        print("You can become a backend developer")

    case "Solidity":
        print("You can become a Blockchain developer")

    case "Java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")




print("\nSimple text calculator:")
a = float(input("Enter First number: "))
b = float(input("Enter Second number: "))
op = input("Enter Operation (sum/sub/mul/div): ")

match op:
    case "sum":
        print(f"a + b = {a+b}")
    case "sub":
        print(f"a - b = {a-b}")
    case "mul":
        print(f"a * b = {a*b}")
    case "div":
        print(f"a / b = {a/b}")
    case _:
        print("Invalid Operation!")
