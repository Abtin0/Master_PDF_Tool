import os
import shutil
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
    columns = shutil.get_terminal_size().columns
    ascii_art = r'''
  _____  _____  ______   _____  _____   ____   _____ ______  _____ _____ _____ _   _  _____   _______ ____   ____  _      
 |  __ \|  __ \|  ____| |  __ \|  __ \ / __ \ / ____|  ____|/ ____/ ____|_   _| \ | |/ ____| |__   __/ __ \ / __ \| |     
 | |__) | |  | | |__    | |__) | |__) | |  | | |    | |__  | (___| (___   | | |  \| | |  __     | | | |  | | |  | | |     
 |  ___/| |  | |  __|   |  ___/|  _  /| |  | | |    |  __|  \___ \\___ \  | | | . ` | | |_ |    | | | |  | | |  | | |     
 | |    | |__| | |      | |    | | \ \| |__| | |____| |____ ____) |___) |_| |_| |\  | |__| |    | | | |__| | |__| | |____ 
 |_|    |_____/|_|      |_|    |_|  \_\\____/ \_____|______|_____/_____/|_____|_| \_|\_____|    |_|  \____/ \____/|______|
                                                                                                                          
                                                                                                                          '''
    print(ascii_art.center(columns))

    print("1. Export Pages".center(columns))
    print("2. Extract Text".center(columns))
    print("3. Lossless Compression".center(columns))
    print("4. Merge PDFs".center(columns))
    print("5. Split PDF".center(columns))
    print("6. Exit".center(columns))


def main():
    """Main program loop."""
    columns = shutil.get_terminal_size().columns
    while True:
        clear_screen()
        show_menu()

        choice = input("\nEnter your choice: ")

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
            print("Invalid choice. Please try again.".center(columns))

        input("\nPress Enter to return to the menu...".center(columns))


if __name__ == "__main__":
    main()
