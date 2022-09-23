import PyPDF2

# Accessing the PDF file
# Add the file location here
a = PyPDF2.PdfFileReader('<here>')

str = ""
# Extracting the text
for i in range(0, a.getNumPages()):
    str += a.getPage(i).extractText()

# Creating text file and writing the extracted text to it.
with open("text.txt", "w", encoding="utf-8") as f:
    f.write(str)
