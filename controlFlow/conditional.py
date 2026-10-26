age = input("Please enter your age: ")

if(int(age) > 18):
    print("You are an adult.")
elif(int(age) == 18):
    print("You are 18 years old.")
else:
    print("You are not an adult.")