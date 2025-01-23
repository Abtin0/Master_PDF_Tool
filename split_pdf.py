from pypdf import PdfWriter, PdfReader
import utils
import os


def split_pdf():
    while True:
        # Get the file path and validate it
        path = input("Please enter filename: ")
        base_name = path
        path = utils.input_extention(path)
        if os.path.isfile(path):
            break
        else:
            print(f'"{path}" is not a valid file. Please try again.')

    # Open the PDF file
    with open(path, "rb") as pdf_file:
        reader = PdfReader(pdf_file)

        # Loop through pages and write each to a separate file
        for i, page in enumerate(reader.pages):
            writer = PdfWriter()
            writer.add_page(page)
            output_filename = f"{base_name}-page-{i + 1}.pdf"
            if not os.path.exists("output"):
                os.makedirs("output")
            with open("output/"+output_filename, "wb") as output_file:
                writer.write(output_file)
                print(f'Page {i + 1} saved as "{output_filename}".')

    print("PDF splitting completed successfully.")


if __name__ == "__main__":
    split_pdf()
