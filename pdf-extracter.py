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
