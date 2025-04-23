1.
[
    {
        "ism": "Ali",
        "familiya": "Valiyev",
        "yosh": 20,
        "fakultet": "Informatika"
    },
    {
        "ism": "Laylo",
        "familiya": "Qodirova",
        "yosh": 22,
        "fakultet": "Matematika"
    }
]

import json
with open("students.json", "r", encoding='utf-8') as file:
    data=json.load(file)
    # print(data)
    for talaba in data:
        print(f"  Ism: {talaba['ism']}")
        print(f"  Familiya: {talaba['familiya']}")
        print(f"  Yosh: {talaba['yosh']}")
        print(f"  Fakultet: {talaba['fakultet']}")
        print()

2.

import requests as r
import json

url = "https://api.openweathermap.org/data/2.5/weather?lat=41.3123363&lon=69.2787079&appid=4c64ec380eda4ba57ee01de480f290b4&units=metric"

res = r.get(url)
data = res.json()
print(data)

import json

with open('jobs.json', 'r',  ) as file:
    data = json.load(file)
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    weather_description = data['weather'][0]['description']
    wind_speed = data['wind']['speed']
    CITY = 'Tashkent'

    
    print(f"Weather in {CITY}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Weather Description: {weather_description.capitalize()}")
    print(f"Wind Speed: {wind_speed} m/s")
3.
import json
import os

BOOKS_FILE = 'books.json'

def load_books():
    if not os.path.exists(BOOKS_FILE):
        return []
    with open(BOOKS_FILE, 'r') as f:
        return json.load(f)

def save_books(books):
    with open(BOOKS_FILE, 'w') as f:
        json.dump(books, f, indent=4)

def add_book():
    books = load_books()
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    year = input("Enter year of publication: ")

    book = {
        "id": len(books) + 1,
        "title": title,
        "author": author,
        "year": year
    }
    books.append(book)
    save_books(books)
    print("Book added successfully.\n")

def update_book():
    books = load_books()
    book_id = int(input("Enter the ID of the book to update: "))
    for book in books:
        if book["id"] == book_id:
            print(f"Current title: {book['title']}")
            book["title"] = input("Enter new title (leave blank to keep current): ") or book["title"]

            print(f"Current author: {book['author']}")
            book["author"] = input("Enter new author (leave blank to keep current): ") or book["author"]

            print(f"Current year: {book['year']}")
            book["year"] = input("Enter new year (leave blank to keep current): ") or book["year"]

            save_books(books)
            print("Book updated successfully.\n")
            return
    print("Book ID not found.\n")

def delete_book():
    books = load_books()
    book_id = int(input("Enter the ID of the book to delete: "))
    updated_books = [book for book in books if book["id"] != book_id]
    if len(updated_books) == len(books):
        print("Book ID not found.\n")
    else:
        save_books(updated_books)
        print("Book deleted successfully.\n")

def list_books():
    books = load_books()
    if not books:
        print("No books found.\n")
        return
    for book in books:
        print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | Year: {book['year']}")
    print()

def main():
    while True:
        print("=== Book Manager ===")
        print("1. List books")
        print("2. Add book")
        print("3. Update book")
        print("4. Delete book")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            list_books()
        elif choice == '2':
            add_book()
        elif choice == '3':
            update_book()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.\n")


    main()
