# import pandas as pd
#
# # Чтение файла с тремя столбцами, исключая первую строку
# df = pd.read_csv('DATA_TXT/RUN010_dE2E5.txt', header=None, names=['bin1', 'bin2', 'count'], skiprows=1)
#
# # Удаление строк, где значение в третьем столбце равно 0
# df = df[df['count'] != 0]
#
# # Создание нового файла для сохранения обновленных данных
# with open('DATA_TXT_CLEAN/RUN010_dE2E5c.txt', 'w') as f:
#     f.write('bin1\tbin2\tcount\n')  # Запись заголовка
#     df.to_csv(f, index=False, header=False, sep='\t')  # Запись обновленных данных


import pandas as pd

# Чтение файла с тремя столбцами, исключая первую строку
df = pd.read_csv('DATA_TXT/RUN010_dE2E5.txt', header=None, names=['x', 'y', 'z'],
                 delim_whitespace=True, skiprows=1)

# Удаление строк, где значение в третьем столбце равно 0
df = df[df['z'] != 0]

# Создание нового файла для сохранения обновленных данных
with open('DATA_TXT_CLEAN/RUN010_dE2E5c.txt', 'w') as file:
    file.write(df.to_string(header=False, index=False))
