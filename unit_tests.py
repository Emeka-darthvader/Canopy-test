import pandas as pd
from standardize_input import standardize_date, standardize_number


df = pd.DataFrame({'normalCurrency':['1,000,000.00'],'dollarCurrency':['$1,000,000.00'],'poundCurrency':['£1,000,000.00'], 'date':['31.03.2018'] })
def test_date_formatting():
    assert (standardize_date(df.date) == "2018/03/31").bool(), "Should be 2018/03/31"

def test_number_formatting():
   assert (standardize_number(df['normalCurrency']) == "1000000.00").bool(), "Should be 1000000.00" #testing normal currency
   assert (standardize_number(df['dollarCurrency'],"$") == "1000000.00").bool(), "Should be 1000000.00" #testing dollar currency
   assert (standardize_number(df['poundCurrency'],"£") == "1000000.00").bool(), "Should be 1000000.00" #testing pound currency

if __name__ == "__main__":
    test_date_formatting()
    test_number_formatting()
    print("All tests passed. Good to go 😊")