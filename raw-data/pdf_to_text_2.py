import os
import PyPDF2

pdf_directory = '/Users/garrett/Desktop/game_book_pdfs'
output_directory = '/Users/garrett/Desktop/pbp_all'

for filename in os.listdir(pdf_directory):
    if filename.endswith('.pdf'):
        pdf_file = os.path.join(pdf_directory, filename)
        
        with open(pdf_file, 'rb') as f:
            pdf_reader = PyPDF2.PdfReader(f)
            txt_filename = os.path.splitext(filename)[0] + '.txt'
            txt_file = os.path.join(output_directory, txt_filename)

            with open(txt_file, 'w') as txt:
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    text = page.extract_text()
                    txt.write(text)
        print(f"Converted {pdf_file} to {txt_file}")
