# importing required modules
from PyPDF2 import PdfReader
 
# creating a pdf reader object
reader = PdfReader('/Users/garrett/Desktop/game_book_pdfs/49ers_at_bears_2022_reg_1.pdf')
 
# printing number of pages in pdf file
print(len(reader.pages))

l = len(reader.pages)

# getting a specific page from the pdf file
page = reader.pages[7]
 
# extracting text from page
text = page.extract_text()

text_file = open(r'/Users/garrett/Desktop/pbp_pdfs/kc_phi.txt', 'w')

text_file.write(text)

text_file.close()




