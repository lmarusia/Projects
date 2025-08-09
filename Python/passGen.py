import random

capLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowLetters = "abcdefghijklmnopqrstuvwxyz"
nums = "1234567890"
symbols = "!@#$%^&*"


use = capLetters + lowLetters + nums + symbols
default = 14

print("\n Welcome to Password Generator")
print("*****************************")

user = input("Would You Like to Generate a Password (y/n)")

while user != "n":

    if user == "y":
        length = int(input("Password Length (8-30): "))
        if length > 8 and length < 30:
            password = "".join(random.sample(use, length))

        else:
            password = "".join(random.sample(use, default))

        print("Your Generated Password: " + password)
        user = input("Would You Like to Generate a Password (y/n)")

print("Thank You For Using Password Generator")
print("**************************************")
print("\n Good Bye!!! \n")