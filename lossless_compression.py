from pypdf import PdfWriter
import utils
import os


def lossless_compression():
    while True:
        path = utils.input_extention(input("Please enter the name of the pdf file: "))
        if os.path.isfile(path):
            writer = PdfWriter(utils.input_extention(path))

            for page in writer.pages:
                page.compress_content_streams()
            if not os.path.exists("output"):
                os.makedirs("output")
            with open(f"output/compressed-document-{path}", "wb") as f:
                writer.write(f)
                print(f'Compressed PDF saved as "compressed-document-{path}".')
                break
        else:
            print("File does not exist.")


if __name__ == "__main__":
    lossless_compression()