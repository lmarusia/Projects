#Basic CLI Text Editor which allows the user to create or edit txt documents \
print("CLI Text Editor")
print("_________________")

choice = input("Would you like to create a new document (n) or edit an existing document (e) or Quit (quit): ")
choice = choice.lower()

#Function that allows the user to open an existing documents content and add additional information
def editDoc():
    fileName = input("Enter File Name: ")
    writing = ""

    with open(fileName, "r") as file:
        writing += file.read()
        userWriting = input(writing)

    with open(fileName, "w") as newFile:
        newFile.write(writing + userWriting)

#Function to handle creating a new document       
def newDoc():
    fileName = input("Enter File Name: ")
    userWrite = input("Press ENTER when Finished -> ")

    with open(fileName, "w") as newFile:
       newFile.write(userWrite)

while choice != "quit":

    if choice  == "n":
        newDoc()


    elif choice == "e":
        editDoc()

    else:
        choice = input("Would you like to create a new document (n) or edit an existing document (e) or Quit (quit): ")