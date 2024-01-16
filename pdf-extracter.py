import pdfplumber
import pandas as pd
import re

def extract_text_from_pdf(pdf_path):
    # Open the PDF file at the specified path using pdfplumber
    with pdfplumber.open(pdf_path) as pdf:
        full_text = []  # Initialize an empty list to store the extracted text

        # Iterate through each page in the PDF
        for page in pdf.pages:
            text = page.extract_text()  # Extract text from the current page

            # Check if there is any text extracted from the page
            if text:
                full_text.append(text)  # Append the extracted text to the list

        # Join all the extracted text into a single string, separated by newlines
        return "\n".join(full_text)

def extract_values(text, term):
    # Define a regular expression pattern to match the specified term followed by a series of financial figures
    # The pattern is dynamically constructed using the term provided
    pattern = fr'{re.escape(term)}[^¥$]*[¥$][0-9,\(\)-]+(?: [¥$][0-9,\(\)-]+)+'

    # Use re.findall to search for all occurrences of the pattern in the provided text
    return re.findall(pattern, text)


def main():
    # Specify the path to your PDF file
    pdf_path = 'path_to_your_pdf.pdf'  # Replace with the actual PDF file path

    # Extract text from the PDF
    pdf_text = extract_text_from_pdf(pdf_path)

    # Define the term to search for
    search_term = "Gains (losses) on other investments"

    # Extract values associated with the search term from the PDF text
    extracted_values = extract_values(pdf_text, search_term)

    # Print or process the extracted values
    for value in extracted_values:
        print(value)

if __name__ == "__main__":
    main()
