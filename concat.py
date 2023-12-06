import pandas as pd

# Читаем данные из файлов
df1 = pd.read_excel('Results1b.xlsx')
df2 = pd.read_excel('Results1a.xlsx')

# Объединяем данные
df = pd.concat([df1, df2], ignore_index=True)

# Записываем объединенные данные в новый файл
df.to_excel('Results1ab.xlsx', index=False, header=False)
