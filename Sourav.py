import pandas as pd 

file = 'Book1.xlsx'

df = pd.read_excel(file, index_col=False)
print(df)
