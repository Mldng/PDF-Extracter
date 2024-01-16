import pdfplumber
import pandas as pd
import re
import os

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

    matches = re.findall(pattern, text)

    # Extract only the numeric values from each match
    values = []
    for match in matches:
        numbers = re.findall(r'[¥$][0-9,\(\)-]+', match)
        values.extend(numbers)
    return values

def save_csv(df, term):
    print(f'Saving data for {term}')
    save_path = os.path.join(os.getcwd(),'csv')
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    save_name = f'{save_path}/{term}.csv'
    df.to_csv(save_name, index=False)
    print(f'finished saving data for {term}')

def main():
    # Specify the path to your PDF file
    pdf_path = 'afr2022.pdf'  # Replace with the actual PDF file path

    # Extract text from the PDF
    pdf_text = extract_text_from_pdf(pdf_path)

    # Define the term to search for
    search_term = "Gains (losses) on other investments"

    # Extract values associated with the search term from the PDF text
    extracted_values = extract_values(pdf_text, search_term)

    # Create a DataFrame with the extracted values
    df = pd.DataFrame(extracted_values, columns=['Extracted Values'])

    # Save the DataFrame to a CSV file
    save_csv(df,search_term)

if __name__ == "__main__":
    main()
