import PyPDF2
import os

# Create a PdfMerger object
merger = PyPDF2.PdfMerger()

# Iterate over the files in the current working directory
for file in os.listdir(os.curdir):
    # If the file ends with ".pdf", add it to the merger
    if file.endswith(".pdf"):
        merger.append(file)

# Write the combined PDF to a file called "combined.pdf"
merger.write("combined.pdf")
