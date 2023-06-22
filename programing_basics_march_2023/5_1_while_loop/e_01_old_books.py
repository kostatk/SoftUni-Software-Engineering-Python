favorite_book = input()

book_counter = 0

while True:
    picked_book = input()

    if picked_book == favorite_book:
        print(f"You checked {book_counter} books and found it.")
        break

    elif picked_book == "No More Books":
        print(f"The book you search is not here!")
        print(f"You checked {book_counter} books.")
        break

    book_counter += 1
