from pypdf import PdfWriter
import utils
import os.path


def export_pages():
    merger = PdfWriter()

    while True:
        path = utils.input_extention(input("Please enter filename: "))
        if os.path.isfile(path):
            fileobj = open(path, "rb")
            break
        else:
            print(f"{path} is not a valid file.")

    while True:
        pages = input("Please enter the pages you want to export (e.g., '1-4' for a range or '1,4' for specific pages): ")
        try:
            if "-" in pages:  # Process input as a range of numbers (tuple)
                start, end = map(int, pages.split("-"))
                pages = (start - 1, end)  # Convert to zero-based indexing for the start
                merger.append(fileobj=fileobj, pages=pages)
                break

            elif "," in pages:  # Process input as specific pages (list)
                pages = list(map(lambda x: int(x) - 1, pages.split(",")))  # Convert all to zero-based indexing
                merger.append(fileobj=fileobj, pages=pages)
                break

            elif pages.isdigit():  # Process single page input
                page = int(pages) - 1  # Convert to zero-based indexing
                merger.append(fileobj=fileobj, pages=[page])
                break

            else:
                print("Invalid format for pages. Please use '-' for a range or ',' for specific pages.")

        except IndexError:
            print("Page does not exist. Please enter valid page number.")

    # Write to an output PDF document
    if not os.path.exists("output"):
        os.makedirs("output")
    output = open(f"output/exported-document-{path}", "wb")
    merger.write(output)
    print(f'PDFs merged successfully as "exported-document-{path}".')

    # Close File Descriptors
    merger.close()
    output.close()


if __name__ == "__main__":
    export_pages()
