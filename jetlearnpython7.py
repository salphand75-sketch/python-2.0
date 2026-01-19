while True:
    choice = int(input("What do you want to do; 1, Add new note, 2, Read all notes, 3, Clear file or 4, Stop "))
    if choice == 1:
        note = input("What do you want to add? ")
        file = open("file.txt","a")
        file.write(note)
        file.close
    elif choice == 2:
        with open("file.txt","r")as file:
            note2 = file.read()
            print(note2)
    elif choice == 3:
        file = open("file.txt","w")
        file.write("")
        file.close()
    elif choice == 4:
        break
    else:
        print("Invalid option")