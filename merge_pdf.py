from os.path import split

from pypdf import PdfWriter
import utils
import os.path


def merge_pdf():
    merger = PdfWriter()

    while True:
        raw_list = utils.input_to_list(input("Please enter filenames in order (file1.pdf, file2.pdf, etc.): "))
        input_list = []
        for i in raw_list:
            input_list.append(utils.input_extention(i))

        if len(input_list) >= 2:
            files = {}
            for selected_pdf in input_list:
                if os.path.isfile(selected_pdf):
                    files[selected_pdf] = open(selected_pdf, "a")
                else:
                    print(f"{selected_pdf} is not a valid file. Please enter valid filenames.")
                    break
            else:
                break
        else:
            print("Please enter 2 filenames or more.")

    action = input("0. Merge whole PDFs\n1. Merge certain pages\nSelect an option:  ")
    if action == "0":
        for pdf in files:
            merger.append(pdf)

    if action == "1":
        while True:
            split_file = utils.input_extention(input("Please enter which file you want to use pages from: "))
            if os.path.isfile(split_file):
                break
            else:
                print(f"{split_file} is not a valid file. Please enter a valid filename.")

        for pdf in files:
            if pdf == split_file:
                continue
            merger.append(pdf)
        while True:
            pages = input("Please enter the pages you want to merge (e.g., '1-4' for a range or '1,4' for specific pages): ")
            try:
                if "-" in pages:  # Process input as a range of numbers (tuple)
                    start, end = map(int, pages.split("-"))
                    pages = (start - 1, end)  # Convert to zero-based indexing for the start
                    merger.append(fileobj=split_file, pages=pages)
                    break

                elif "," in pages:  # Process input as specific pages (list)
                    pages = list(map(lambda x: int(x) - 1, pages.split(",")))  # Convert all to zero-based indexing
                    merger.append(fileobj=split_file, pages=pages)
                    break

                elif pages.isdigit():  # Process single page input
                    pages = int(pages) - 1  # Convert to zero-based indexing
                    merger.append(fileobj=split_file, pages=[pages])
                    break

                else:
                    print("Invalid format for pages. Please use '-' for a range or ',' for specific pages.")

            except IndexError:
                print("Page does not exist. Please enter valid page number.")

    # Write to an output PDF document
    output = open("merged-document-output.pdf", "wb")
    merger.write(output)
    print('PDFs merged successfully as "merged-document-output.pdf".')

    # Close File Descriptors
    merger.close()
    output.close()


if __name__ == "__main__":
    merge_pdf()
