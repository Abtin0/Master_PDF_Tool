from pypdf import PdfWriter
import utils

merger = PdfWriter()

input_list = utils.input_to_list(input("Please enter filenames (file1.pdf, file2.pdf, etc.): "))

files = {}

for i, selected_pdf in enumerate(input_list):
    files[f"pdf{i}"] = open(selected_pdf, "w")

# add the first 3 pages of input1 document to output
merger.append(fileobj=input1, pages=(0, 3))

# insert the first page of input2 into the output beginning after the second page
merger.merge(position=2, fileobj=input2, pages=(0, 1))

# append entire input3 document to the end of the output document
merger.append(input3)

# Write to an output PDF document
output = open("document-output.pdf", "wb")
merger.write(output)

# Close File Descriptors
merger.close()
output.close()
