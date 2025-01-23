from pypdf import PdfReader
import utils


def extract_text():
    while True:
        try:
            path = input("Please enter the name of the pdf file: ").lower()
            reader = PdfReader(utils.input_extention(path))
            break
        except FileNotFoundError:
            print("File not found.")

    while True:
        try:
            num_pages = input(
                f"There are {len(reader.pages)} pages in {path}. Select the pages you want to extract (1,2,3 etc.):")
            for selected_page in utils.input_to_list(num_pages):
                page = reader.pages[int(selected_page) - 1]
                with open(path.replace(".pdf", ".txt") if ".pdf" in path else path + ".txt", "w") as text_file:
                    text_file.write(page.extract_text()+"\n")
                    print(f"Extracted text for page {selected_page}")
            break

        except IndexError:
            print(f"Page {selected_page} does not exist. Please try again.")

        except ValueError:
            print("Please enter a number.")

    print("Extraction complete.")


if __name__ == "__main__":
    extract_text()
