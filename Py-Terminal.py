import shutil as sh

def copy(oldFile, newFile):
    sh.copy(oldFile, newFile)

def move(oldFile, newFile):
    sh.move(oldFile, newFile)

user = input("> ")

if not user.lower() == "exit":
  
    command = user.split()
    cmd = command[0]
    file = command[1]
    new = command[2]

    while not user == "exit":    
        if cmd == "cp":
            copy(file, new)

        elif cmd == "mv":
            move(file, new)

        user = input("> ")  

        if user.lower() == "exit":
            break
        else:    
            cmd, file, new, = user.partition(" ")
