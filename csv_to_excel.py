import argparse
import pandas as pd
from standardize_input import standardize_number, standardize_date
from helper_modules.response_messages import success_cleaned,success_exported



#get the arguments parsed
parser = argparse.ArgumentParser()
parser.add_argument("-d","--data", help="Directory for text file to be transformed to excel",default="data/cleaned_canopy_technical_test_input.txt")
parser.add_argument("-f","--filename", help="name for new Excel file",default="excel_files/canopy_technical_test_input.xlsx")
args = parser.parse_args()

#Function to read and clean txt file generated
def read_and_clean_csv(datasource):
    df = pd.read_csv(datasource,sep="*",quotechar='"')

    #search if dataframe column name contains keywords date (denoting time) and standardize
    date_cols = [col for col in df.columns if 'Date' in col]
    for date in date_cols:
        df[date] = standardize_date(df[date])
    
    #search if dataframe column name contains keywords Balance, Credit, Debit (denoting currency) and standardize
    currency_keywords = ["Balance","Credit","Debit"]
    currency_cols = [currency  for col in df.columns for currency in currency_keywords   if currency in col]
    
    for currency in currency_cols:
        df[currency] = standardize_number(df[currency])
    
    success_cleaned()
    return df


#Function to export dataframe to Excel
def export_to_excel(df,xls_file_name):
    writer = pd.ExcelWriter(xls_file_name, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', index=True)
    workbook=writer.book
    worksheet = writer.sheets['Sheet1']
    format = workbook.add_format({'text_wrap': False})
    worksheet.set_column('C:C',None, format)
    writer.save()
    success_exported()

    


#load txt file into dataframe and clean
cleaned_dataframe = read_and_clean_csv(args.data)

#transform cleaned dataframe into excel
export_to_excel(cleaned_dataframe,args.filename)