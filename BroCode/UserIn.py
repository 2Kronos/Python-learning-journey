# name = input("Enter your name:")
# age = int(input ("Enter your age ")) # input will give you a string data type so you will need to change it
# #age = int(age) # Can be done in one line 
# age = age +1
# print(f"Hello {name}")
# print(f"You are {age} years old")

#====================================== MADLIB GAME=====================================7

# adjective1 = input("Enter an adjective: ")
# noun = input("Enter an noun: ")
# verb = input("Enter an verb: ")
# adjective2 = input("Enter an adjective2: ")
# verb = input("Enter an verb: ")
# adjective3 =input("Enter an adjective3:")

# print(f"Today I went to a {adjective1} zoo")
# print(f"In an exibit, I saw a {noun}")
# print(f"{noun} was {adjective2} and {verb}ing")
# print(f"I was {adjective3}")

# =============================== AREA OF A RECTANGLE =================================

# lenght = float(input("Enter the width of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))
# height  =  float(input("Enter the height of the rectangle: "))

# volume = lenght * width * height 

# print(f"The area is: {volume}cm^3")


# =========================== Shopping cart programme ================================================
item = input("What is the item you want to buy: ")
price = float(input("What is the price: "))
quantity = int(input("How many would you like: "))
total = price * quantity

print(f"You have bought {quantity} X {item}/s")
print(f"Your total is {round(total, 2)}$")