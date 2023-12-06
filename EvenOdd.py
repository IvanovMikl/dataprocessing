import pandas as pd

# Read excel file
df = pd.read_excel('Results.xlsx')

# Save odd line
df = df[df.index % 2 != 0]

# Write new excel file
writer = pd.ExcelWriter('Results1a.xlsx')
df.to_excel(writer)
writer.close()


# Read excel file
df = pd.read_excel('Results.xlsx')

# Save even line
df = df[df.index % 2 == 0]

# Write new excel file
writer = pd.ExcelWriter('Results1b.xlsx')
df.to_excel(writer)
writer.close()
