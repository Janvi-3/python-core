import json
import os
LIBRARY_PATH=r"C:\Users\Dell\OneDrive\Desktop\python project\Personal_library_manager\library.json"
def load_library():
    if os.path.exists(LIBRARY_PATH):
        try:
            with open(LIBRARY_PATH,'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
                return[]
    else:
        return[]

def save_Library(books):
    with open(LIBRARY_PATH,'w') as f:
        json.dump(books,f,indent=4)

def add_book():
    print("\n ADD NEW BOOK")
    title=(input("tiltle : "))
    author=input("Author: ")

    book ={
        'title':title,
        'author':author,
        'read':False
    }
    library.append(book)
    save_Library(library) 
    print(f"\n '{title}' added successfully")

def show_books():
    print("\n Your Books: ")
    if not library:
        print("Your library is empty. ")
        return
    for i , book in enumerate(library,1) :
        status= "Read " if book ['read'] else "Not read"
        print(f"{i}. {book['title']} by {book['author']}-{status}")
    
def mark_read():
    show_books()
    if not library:
        return
    try:
        num=int(input("Enter book number to mark as a read "))
        if 1<=num<=len(library):
            library[num-1]['read']=True
            save_Library(library)
            print(f"Marked'{library[num-1]['title']}' as read")
        else:
            print("Invalid Number")
    except ValueError:
        print("Please Enter a valid number")

def delete_book():
    show_book()
    if not library:
        return
    try:
        num=int(input("Enter book number to delete:"))
        if 1<=num<=len(library):
            removed=library.pop(num-1)
            save_Library(library)
            print(f"Removed '{removed['title']}'from your library")
        else:
            print("Invalid Number")
    except ValueError:
        print("Please Enter a valid number")


library=load_library()
while True:
    print("/n PERSONAL LIBRARY MANAGER")
    print("1. Add Book")
    print("2. View books")
    print("3. Mark as a read")
    print("4. Delete Book")
    print("5. Exit")


    choice=input("ENTER YOUR CHOICE (1-5):")

    if choice=="1":
        add_book()
    elif choice=="2":
        show_books()
    elif choice=="3":
        mark_read()
    elif choice=="4":
        delete_books()
    elif choice =="5":
        print(" GOODBYE ")
        break
    else :
        print(" Invalid choice . Please try again ")