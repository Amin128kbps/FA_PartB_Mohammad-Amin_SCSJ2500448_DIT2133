from library_module import Book

books = {
    "Python 101": "Philip Robbins",
    "Data Science": "Jannah Mohd"
}

title = input("Enter book title")
author = input("Enter book author")
books[title] = author

with open ("books.txt", "w") as f:
    for t, a in books.items():
        f.write (f"{t}: {a}\n")

with open ("books.txt", "r") as file:
    lines = file.readlines()

print("\n Book list from File: ")
for line in lines:
    t, a = line.strip().split (":")
    b = books (t, a)
    b.display_info()
