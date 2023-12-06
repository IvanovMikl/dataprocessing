import pandas as pd

# Reading the csv file
df_new = pd.read_csv('Results.csv')

# saving xlsx file
GFG = pd.ExcelWriter('Results.xlsx')
df_new.to_excel(GFG, index=False)

GFG.close()
