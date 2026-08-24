books = ["Diary of a Wimpy Kid", "Dog Man", "Lion King", "Lord of The Flies", "Library Lion"]

print("Library Book List:", books)

print("Total Books:", len(books))
print("First Book:", books[0])
print("Last Book:", books[-1])
print("First Three Books:", books[:3])

books.append("Captain underpants")
print("After Adding a Book:", books)

books.remove("Lion King")
print("After Removing a Book:", books)

books.sort()
print("Books Sorted Alphabetically:", books)

books.reverse()
print("Books in Reverse Order:", books)

librarian = {
    "name": "Mr.Griffin ",
    "section": "Comic",
    "experience": 12
}

print("Librarian Profile:", librarian)

print("Librarian Name:", librarian["name"])
print("Library Section:", librarian["section"])
print("Amount of experience:", librarian.get("experience"))

librarian["experience"] = 6
print("Updated Experience:", librarian)

librarian["email"] = "roziel@coolteacher.com"
print("After Adding Email:", librarian)

librarian.pop("section")
print("After Removing Section:", librarian)

book_ids = [251, 252, 253, 254, 255]
book_names = ["Diary of a Wimpy Kid", "Dog Man", "Lion King", "Lord of The Flies", "Captain Underpants"]

book_directory = dict(zip(book_ids, book_names))

print("Book Directory:", book_directory)

print("LIBRARY ORGANISER SUMMARY")
print("================================")
print("Available Books:", books)
print("Librarian Details:", librarian)
print("Book ID Directory:", book_directory)