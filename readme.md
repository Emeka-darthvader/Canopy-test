# Canopy Technical Test #
Thank you for the opportunity. The following are steps on how I attempted the problem:

1. Extract the text from the pdf using poppler. To extract the text from pdf, kindly run the pdf_to_txt.py file and supply -d / --data as an argument (directory where the pdf file to be extracted is). For example: python pdf_to_txt.py --data data/canopy_technical_test_input.pdf. If no argument is provided it uses the default: data/canopy_technical_test_input.pdf. The poppler command used in the code is - pdftotext data/canopy_technical_test_input.pdf  -nodiag -layout
2. Preprocess the extracted text. To do this, run the preprocess.py and supply -f/--filename as the directory where your extracted text resides. The default argument is data/canopy_technical_test_input.pdf.
3. Perform Data Cleaning on the extracted text. This includes checking the quality, adding delimeters
4. Load the cleaned dataset and transform to pdf. Run csv_to_excel.py supplying -d/--data for the directory of the cleaned dataset and -f/--filename for the name of the excel file to output. The default value for data is data/cleaned_canopy_technical_test_input.txt while for filename is excel_files/canopy_technical_test_input.xlsx

### Unit Tests ###
The unit tests while written and can be run using unit_tests.py

### Other Files ###
1. standardize_input.py. This file contains implementation for date and number formatting
2. helper_modules/response_messages.py. This file contains implementation for response messages