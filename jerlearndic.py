books = {"Harry Potter": "J.K. Rowling", "Moby-Dick": "Herman Melville", "The lord of the rings":"JRR Tolkien"}
print(books["Harry Potter"])
print(books)
books["Charlie and the chocolate factory"] = "Roald Dahl"
print(books)
books["The lord of the rings"] = "J.R.R Tolkien"
print(books)
del books["Moby-Dick"]
print(books)
for book in books:
    print(book,"-",books[book])
for k,v in books.items():
    print(k,v)
books.update({"Moby-Dick":"Herman Melville"})
print(books)
books.update({"Harry Potter":"JK Rowling"})
print(books)
print(books.items())
print(books.keys())
print(books.values())