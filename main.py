import sys
from PyPDF2 import PdfReader

args = sys.argv[1:]
path_file = args[0]

reader = PdfReader(path_file)

for i in range(len(reader.pages)):
    print("Page:", i)
    print(reader.pages[i].extract_text())
