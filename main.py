import os
import export_pages
import extract_text
import lossless_compression
import merge_pdf
import split_pdf

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    """Display the main menu."""
    print("PDF Processing Tool")
    print("-------------------")
    print("1. Export Pages")
    print("2. Extract Text")
    print("3. Lossless Compression")
    print("4. Merge PDFs")
    print("5. Split PDF")
    print("6. Exit")

def main():
    """Main program loop."""
    while True:
        clear_screen()
        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            export_pages.export_pages()  # Call the function from the module
            clear_screen()
        elif choice == "2":
            extract_text.extract_text()  # Call the function from the module
            clear_screen()
        elif choice == "3":
            lossless_compression.lossless_compression()  # Call the function
            clear_screen()
        elif choice == "4":
            merge_pdf.merge_pdf()  # Call the function
            clear_screen()
        elif choice == "5":
            split_pdf.split_pdf()  # Call the function
            clear_screen()
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main()
