# PDF Data Extractor

## Overview
This project includes a Python script that extracts specific numerical data from a PDF file. It focuses on extracting all numeric values associated with the term "Gains (losses) on other investments". The script reads a PDF, searches for the specified term, extracts the associated numbers, and then saves these numbers to a CSV file.

## Prerequisites
Before running the script, ensure you have the following installed:
- Python 3.x
- Libraries: `pdfplumber` and `pandas`. You can install these using the provided `requirements.txt` file.

## Installation
1. Clone this repository or download the source code.
2. Navigate to the project directory and install the required libraries:
```
pip install -r requirements.txt
```

## Usage
1. Place the PDF file you want to process in an accessible directory.
2. Open `main.py` and modify the `pdf_path` variable to the path of your PDF file:
```python
pdf_path = 'path_to_your_pdf.pdf'
```
3. Run the script:
```css
python main.py
```
4. Once completed, the script will generate a CSV file named extracted_numbers.csv in the project directory containing the extracted values.

## Functionality
- extract_text_from_pdf: Reads and extracts text from each page of the PDF.
- extract_values: Uses a regular expression to find and extract numeric values related to a specified search term from the text.
- main: Orchestrates the reading of the PDF, extraction of values, and saving of these values to a CSV file.

