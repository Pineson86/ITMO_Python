import pandas as pd
from sqlalchemy import create_engine
import numpy as np
import os

# Определяем путь к файлу данных
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'recipes_full_0.csv')
# Загружаем данные в DataFrame
recipes_df = pd.read_csv(file_path)

# Преобразуем дату отправления в формат datetime
recipes_df['submitted'] = pd.to_datetime(recipes_df['submitted'])

# 1. Найдите максимум в столбце n_steps
max_n_steps = recipes_df['n_steps'].max()
print("Максимум в 'n_steps':", max_n_steps)

# 2. Количество отзывов с группировкой по месяцам добавления
monthly_reviews = recipes_df.groupby(recipes_df['submitted'].dt.to_period('M')).size()
print("Количество отзывов по месяцам:\n", monthly_reviews.head())

# 3. Найдите пользователя, отправлявшего рецепты чаще всех
top_contributor = recipes_df['contributor_id'].value_counts().idxmax()
print("Пользователь, отправлявший рецепты чаще всех:", top_contributor)

# 4. Самый первый и самый последний по дате отправления рецепт
earliest_recipe = recipes_df.loc[recipes_df['submitted'].idxmin()]
latest_recipe = recipes_df.loc[recipes_df['submitted'].idxmax()]
print("Самый первый рецепт:", earliest_recipe[['id', 'submitted']])
print("Самый последний рецепт:", latest_recipe[['id', 'submitted']])

# 5. Медианы по количеству ингредиентов и времени приготовления
median_ingredients = recipes_df['n_ingredients'].median()
median_minutes = recipes_df['minutes'].median()
print("Медиана по количеству ингредиентов:", median_ingredients)
print("Медиана по времени приготовления:", median_minutes)

# 6. Самый простой рецепт
simplest_recipe = recipes_df.sort_values(by=['n_ingredients', 'minutes', 'n_steps']).iloc[0]
print("Самый простой рецепт:", simplest_recipe[['id', 'name', 'minutes', 'n_ingredients', 'n_steps']])

# 7. Загрузка данных в базу данных SQLite
database_path = os.path.abspath('recipes.db')
engine = create_engine(f'sqlite:///{database_path}')
recipes_df.to_sql('recipes', engine, if_exists='replace', index=False)
print("Данные успешно загружены в базу данных SQLite")

# 8. Отбор рецептов с временем приготовления меньше медианы и количеством шагов меньше среднего
mean_n_steps = recipes_df['n_steps'].mean()
filtered_recipes = recipes_df[(recipes_df['minutes'] < median_minutes) & (recipes_df['n_steps'] < mean_n_steps)]

# Сохранение отфильтрованных данных в CSV
filtered_csv_path = os.path.abspath('filtered_recipes.csv')
filtered_recipes.to_csv(filtered_csv_path, index=False)
print("Отфильтрованные рецепты сохранены в файл:", filtered_csv_path)
