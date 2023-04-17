import os
import pandas as pd

# Получаем список файлов в директории
files = os.listdir('data')
print(files)
#Инициализируем DataFrame
df = pd.DataFrame()

# Итерируемся по каждому файлу и объединяем данные в DataFrame
for file in files:
    if file.endswith('.csv'):
        file_path = os.path.join('data', file)
        temp_df = pd.read_csv(file_path)
        df = pd.concat([df, temp_df], ignore_index=True)

# Записываем объединенный DataFrame в новый файл
output_path = os.path.join('output', 'merged_data.csv')
df.to_csv(output_path, index=False)
