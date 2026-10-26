age = int(input("Please enter your age: "))

match age:
    case age if age > 18:
        print("You are an adult.")
    case age if age == 18:
        print("You are 18 years old.")
    case age if age < 18:
        print("You are not an adult.")
    case _:
        print("Invalid age entered.")    