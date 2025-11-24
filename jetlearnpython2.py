a = ["wash the dishes","mow the lawn","take out the trash","do the landery"]
while True:
    y = (input("chose: view all tasks, add new task, remove a task, change a task, exit. "))
    if y == "view all tasks":
        print(a)
    elif y == "add new task":
        z =  (input("what do you want to add "))
        a.append(z)
        print(a)
    elif y == "remove a task":
        print(a)
        z = (input("what do you want to remove (use name) "))
        a.remove(z)
        print(a)
    elif y == "change a task":
        print(a)
        z = (input("what do you want to change (use name) "))
        c = (input("what do you want to change it to (use name) "))
        b = a.index(z)
        a[b] = c
        print(a)
    elif y == "exit":
        print("shutting down")
        break
    else:
        print("please try again and check spelling")