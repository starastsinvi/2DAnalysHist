
import matplotlib.pyplot as plt
import pandas as pd

# Считываем новый файл
df = pd.read_csv('DATA_TXT_CLEAN/RUN010_dE2E5c.txt', sep='\s+', header=None, names=['x', 'y', 'z'])

# Создаем гистограмму с 8000 бинов для каждой оси
plt.hist2d(df['x'], df['y'], bins=6000, cmap='hot')

# Добавляем подписи осей и заголовок
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Histogram')

# Отображаем гистограмму
plt.show()