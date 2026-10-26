age=34;
name="John"
cgpa=3.5

if(age>=18):
    print("You are an adult.")
    print("Your name is " + name)
    print("Your age is " + str(age)) 
    print("Your CGPA is " + str(cgpa))   
else:
    print("You are not an adult.")

isPresent=True

if(isPresent):
    print("You are present.")


print(type(age))
print(type(name))
print(type(cgpa))
print(type(isPresent))