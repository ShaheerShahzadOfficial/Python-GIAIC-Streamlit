import streamlit as st
import json

# Initialize the library (list of books)
library = []

# Load library from a file (if exists)
def load_library():
    try:
        with open("library.txt", "r") as f:
            global library
            library = json.load(f)
    except FileNotFoundError:
        pass

# Save library to a file
def save_library():
    with open("library.txt", "w") as f:
        json.dump(library, f)

# Add a book to the library
def add_book(title, author, year, genre, read_status):
    book = {
        "title": title,
        "author": author,
        "year": int(year),
        "genre": genre,
        "read_status": True if read_status == "yes" else False
    }
    library.append(book)

# Remove a book from the library
def remove_book(title):
    global library
    library = [book for book in library if book["title"].lower() != title.lower()]

# Search for books by title or author
def search_books(search_type, search_value):
    if search_type == "title":
        return [book for book in library if search_value.lower() in book["title"].lower()]
    elif search_type == "author":
        return [book for book in library if search_value.lower() in book["author"].lower()]

# Display all books in the library
def display_books():
    if library:
        for idx, book in enumerate(library, 1):
            read_status = "Read" if book["read_status"] else "Unread"
            st.write(f"**{idx}.** {book['title']} by {book['author']} ({book['year']}) - *{book['genre']}* - **{read_status}**")
    else:
        st.write("No books in the library. Please add some books to get started.")

# Display statistics
def display_statistics():
    total_books = len(library)
    read_books = len([book for book in library if book["read_status"]])
    if total_books > 0:
        read_percentage = (read_books / total_books) * 100
        st.write(f"Total books: **{total_books}**")
        st.write(f"Percentage read: **{read_percentage:.2f}%**")
    else:
        st.write("No books in the library.")

# Streamlit UI
def main():
    # Add a custom title
    st.set_page_config(page_title="Personal Library Manager", page_icon="📚", layout="wide")
    st.title("📚 Personal Library Manager")

    # Load the library data
    load_library()

    # Sidebar options
    menu = ["Add a book", "Remove a book", "Search for a book", "Display all books", "Display statistics", "Exit"]
    choice = st.sidebar.selectbox("Choose an action", menu)

    # Action: Add a book
    if choice == "Add a book":
        st.subheader("📖 Add a New Book")
        title = st.text_input("Enter the book title:")
        author = st.text_input("Enter the author:")
        year = st.number_input("Enter the publication year:", min_value=0, step=1)
        genre = st.text_input("Enter the genre:")
        read_status = st.radio("Have you read this book?", ("yes", "no"))
        
        if st.button("Add Book"):
            add_book(title, author, year, genre, read_status)
            save_library()
            st.success(f"**'{title}'** added successfully! 🎉")

    # Action: Remove a book
    elif choice == "Remove a book":
        st.subheader("🗑️ Remove a Book")
        title_to_remove = st.text_input("Enter the title of the book to remove:")
        
        if st.button("Remove Book"):
            remove_book(title_to_remove)
            save_library()
            st.success(f"**'{title_to_remove}'** removed successfully! ❌")

    # Action: Search for a book
    elif choice == "Search for a book":
        st.subheader("🔍 Search Books")
        search_type = st.radio("Search by:", ("Title", "Author"))
        search_value = st.text_input(f"Enter the {search_type.lower()}:")
        
        if st.button("Search"):
            results = search_books(search_type.lower(), search_value)
            if results:
                for idx, book in enumerate(results, 1):
                    read_status = "Read" if book["read_status"] else "Unread"
                    st.write(f"**{idx}.** {book['title']} by {book['author']} ({book['year']}) - *{book['genre']}* - **{read_status}**")
            else:
                st.warning("No books found matching your search. Please try again.")

    # Action: Display all books
    elif choice == "Display all books":
        st.subheader("📚 Your Library")
        display_books()

    # Action: Display statistics
    elif choice == "Display statistics":
        st.subheader("📊 Library Statistics")
        display_statistics()

    # Action: Exit
    elif choice == "Exit":
        save_library()
        st.write("Library saved to file. Goodbye! 👋")

# Run the Streamlit app
if __name__ == "__main__":
    main()
st.markdown("---")
st.markdown("Made with ❤️ by [Shaheer Shahzad](https://shaheershahzad.com)")
