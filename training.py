import pandas as pd
import numpy as np

df = pd.read_csv("file.csv")


print(df.head())
print(f'Размерность набора данных (df.shape()):\n',df.shape) # мы увидим информацию о размерности нашего дата фрейма
print('Размерность, нумерация и не числовые значения набора данных (df.info()):\n',df.info()) # покажет информацию о размерности данных и как данные индексируются, количество not-a-number элементов
print('Статистики набора данных (df.describe()):\n',df.describe()) # показывает статистики: count,mean, std,min, 25%-50%-75% percentile, max
print('Количество уникальных значений для каждого столбца (df.nunique()):\n', df.nunique()) # количество уникальных значений для каждого столбца. 