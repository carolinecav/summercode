# first = input("What is your first name?")
# last = input("What is your last name?")
# birthyr = int(input("What is your birth year?"))
# currentyr = 2018
# print("Hello "+ first + " " + last+"!")
# print("{:.0f}".format(birthyr))
# print("{:.3e}".format(currentyr))
# print("You are "+str(currentyr-birthyr)+" years old.")
# print("Your magic percentage is: "+str("{:.3%}".format(birthyr/currentyr)))

x = float(input("Glarkonians, what is the latest x coordinate?"))
y = float(input("Glarkonians, what is the latest y coordinate?"))
z = float(input("Glarkonians, what is the latest z coordinate?"))
storage = int(input("Computer, how many digits can I store?"))//3
xoutput = "{:." + str(storage)+"f}"
print(xoutput.format(x))
print(xoutput.format(y))
print(xoutput.format(z))