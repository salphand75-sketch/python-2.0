books = {"Harry Potter": "J.K. Rowling", "Moby-Dick": "Herman Melville", "The lord of the rings":"JRR Tolkien"}
while True:
    y = (input("chose: view all books, add new book, remove a book, change a book, exit. "))
    if y == "view all books":
        print(books)
    elif y == "add new book":
        z =  (input("what book do you want to add "))
        f = (input("who wrote it? "))
        books[z] = f
        print(books)
    elif y == "remove a book":
        print(books)
        z = (input("what do you want to remove (use name) "))
        del books[z]
        print(books)
    elif y == "change a book":
        print(books)
        z = (input("what auther do you want to change (use name) "))
        c = (input("what do you want to change it to (use name) "))
        books[z] = c
        print(books)
    elif y == "exit":
        print("shutting down")
        break
    else:
        print("please try again and check spelling")