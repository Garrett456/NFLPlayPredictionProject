##################################
#
# This script converts  
# .pdf to .txt
#
##################################


import os
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams

# Set the paths for the input and output directories
input_dir = '/Users/garrett/Desktop/game_book_pdfs'
output_dir = '/Users/garrett/Desktop/pbp_text'pbp_


# Iterate through the PDF files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.pdf'):
        # Set the input and output file paths
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.txt')

        # Extract the text from the PDF file, excluding the first 7 pages
        with open(output_path, 'wb') as output_file:
            extract_text_to_fp(open(input_path, 'rb'), output_file, laparams=LAParams(), page_numbers=range(7, 100000))

print('Done!')


