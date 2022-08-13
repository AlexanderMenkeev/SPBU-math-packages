# -*- coding: utf-8 -*-

# -- Sheet --
https://datalore.jetbrains.com/view/notebook/hgD1hDxGzan4oznHceKExl

import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 22})
#1. Считайте файл
anime_df = pd.read_csv('anime.csv')
#2. Выведите первые 10 строк датафрейма
print(anime_df.head(20).to_string())

#3. Выведите информацию о столбцах
print(anime_df.info())

#4. Приведите названия столбцов к единому виду
# нижний регистр и "_" вместо пробелов
anime_df['New column'] = None
columns = anime_df.columns
print(*columns)
modified_columns = []
for column in columns:
    modified_column = ''
    for character in column:
        if character == ' ':
            modified_column += '_'
        else:
            modified_column += character
            
    modified_columns.append(modified_column.casefold())

anime_df.columns = modified_columns
print(*anime_df.columns)

#5. Для каждого столбца с числами построить статистики
anime_df.voters = anime_df.voters.str.replace(',', '')
anime_df.episodes = pd.to_numeric(anime_df.episodes, errors='coerce')
anime_df.voters = pd.to_numeric(anime_df.voters, errors='coerce')
print(anime_df.describe())

#6. Для каждого из столбцов, содержащих категориальные значения, 
# вывести все возможные значения с количеством их повторений
#Column = "Production"
print(anime_df.production.value_counts().head(20).to_string())

#Column = "Source"
print(anime_df.source.value_counts().to_string())

#7. Заполните пропуски в данных
anime_df.production = anime_df.production.str.replace('-', 'Unknown')
anime_df.source = anime_df.source.str.replace('-', 'Unknown')
anime_df.theme = anime_df.theme.str.replace('-', 'Unknown')
#anime_df.episodes = anime_df.episodes.fillna('Unknown')
anime_df.airdate = anime_df.airdate.fillna('Unknown')

#8.a
anime_companies = anime_df.production.value_counts()
biggest = anime_companies.head(5)
smallest = anime_companies.tail(5)
result = pd.concat([smallest, biggest])
result = result.sort_values()
fig1, ax = plt.subplots(figsize = (18,10))
ax.barh(result.index, result)
ax.set_xlabel("Anime produced", size = 20)
ax.set_title("Anime companies by number of animes", size = 25)
plt.show()

#8.b
numberOfEpisodes = anime_df.episodes.value_counts()
numberOfEpisodes = numberOfEpisodes.sort_index()
numberOfEpisodes = numberOfEpisodes.head(24)
print(numberOfEpisodes)
fig2, ax = plt.subplots(figsize = (18,10))
ax.bar(numberOfEpisodes.index, numberOfEpisodes)
ax.set_xlabel("Number of episodes", size = 15)
ax.set_ylabel("Number of animes", size = 15)
ax.set_title("What number of episodes occurres more often?", size = 25)
plt.show()

#8.c
sources = anime_df.source.value_counts()
print(sources)
sources = sources.head(5)
fig3, ax = plt.subplots(figsize = (15,10))
ax.bar(sources.index, sources)
ax.set_xlabel("Source", size = 15)
ax.set_ylabel("Number of animes", size = 15)
ax.set_title("Top 5 sources of anime", size = 25)
plt.show()

#8.d
strings = anime_df.theme
list_of_themes = []
for string in strings:
    themes = string.split(sep=',') 
    for theme in themes:
        list_of_themes.append(theme)

themes_series = pd.Series(list_of_themes)
themes_series = themes_series.sort_values()
themes_series = themes_series.drop_duplicates()

list_of_themes = []
for theme in themes_series:
    list_of_themes.append([theme, len(anime_df[anime_df.theme.str.contains(theme)])])

df = pd.DataFrame(list_of_themes, columns=['theme', 'number_of_animes'])
df = df.sort_values('number_of_animes', ascending=False)
print(df)
df = df.head(10)
fig, ax = plt.subplots(figsize = (18,10))
ax.barh(df.theme, df.number_of_animes)
ax.set_xlabel("Number of animes", size = 20)
ax.set_title("Top 10 most popular anime themes", size = 30)
plt.show()

#9
rating = pd.Series(float)
companies = anime_df.production.drop_duplicates()
my_list = []
for company in companies:
    rating = anime_df.query("production == @company").rating
    mean = rating.mean()
    my_list.append([company, mean])

df = pd.DataFrame(my_list,columns=['company', 'average_rating'])
df = df.sort_values('average_rating', ascending=False)
print(df.head(20))
df = df.head(20)
fig, ax = plt.subplots(figsize = (18,20))
ax.barh(df.company, df.average_rating)
ax.set_xlabel("Average rating", size = 18)
ax.set_title("Top 20 companies with best anime", size = 30)
plt.show()

#10
my_list = []
for i in range(0, 10):
    number_of_animes = len(anime_df.query("rating >= @i and rating < @i+1"))
    my_list.append(['[' + str(i)+ ', ' + str(i+1) + ')' , number_of_animes] )

df = pd.DataFrame(my_list, columns=['rating_interval', 'number_of_animes'])

fig, ax = plt.subplots(figsize = (18,10))
ax.bar(df.rating_interval, df.number_of_animes)
ax.set_xlabel("Rating intervals", size = 25)
ax.set_ylabel("Number of animes", size = 25)
ax.set_title("Most often occurring rating intervals of animes", size = 30)
plt.show()

#12
fig, ax = plt.subplots(figsize = (50,20))
ax.plot(anime_df.voters, anime_df.rating)
ax.set_xlabel("Number of viewers", size = 30)
ax.set_ylabel("Rating", size = 25)
ax.set_title("Связь между рейтингом аниме и его количеством зрителей", size = 40)
plt.show()

