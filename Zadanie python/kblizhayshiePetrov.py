from calendar import c
import pandas as pd

# Читаем файл, дропаем незаполненные строчки
file = pd.read_csv('./file.csv')
file = file.dropna()
# Маплю название - число
district = {
    'ЦАО': 1,
    'САО': 2,
    'СВАО': 3,
    'ВАО': 4,
    'ЮВАО': 5,
    'ЮАО': 6,
    'ЮЗАО': 7,
    'ЗАО': 8,
    'СЗАО': 9,
    'МО': 10,
}

zodiac = {
    'Овен': 1,
    'Телец': 2,
    'Близнецы': 3,
    'Рак': 4,
    'Лев': 5,
    'Дева': 6,
    'Весы': 7,
    'Скорпион': 8,
    'Стрелец': 9,
    'Козерог': 10,
    'Водолей': 11,
    'Рыбы': 12
}

color = {
    'Черный': 1,
    'Белый': 2,
    'Красный': 3,
    'Синий': 4,
    'Зеленый': 5,
    'Розовый': 6,
    'Фиолетовый': 7,
    'Оранжевый': 8,
    'Салатовый': 9,
    'Голубой': 10,
    'Индиго': 11
}

column = [x for x in file.columns]
# Получаем списоком "шапку таблицы" без колонок ФИО, К/Ч, Любимый 
column = column[1:-1]
test_file = pd.read_csv('./newfile.csv')
dist_neighbor = dict()

for i in file.index:
    distance = abs(district.get(file.loc[i][column[0]])) - district.get((test_file.loc[0][column[0]])) + \
                abs(zodiac.get(file.loc[i][column[1]]) - zodiac.get(test_file.loc[0][column[1]])) + \
                abs(color.get(file.loc[i][column[2]]) - color.get(test_file.loc[0][column[2]])) + \
                abs(float(file.loc[i][column[3]]) - float(test_file.loc[0][column[3]])) + \
                abs(float(file.loc[i][column[4]]) - float(test_file.loc[0][column[4]])) + \
                abs(float(file.loc[i][column[5]]) - float(test_file.loc[0][column[5]]))
    dist_neighbor[i] = distance

k = 3 # Количество соседей
sorted_distance_neighborhood = sorted(dist_neighbor.items(), key=lambda k: k[1])[:k]

answer = {
    'Ч':0,
    'К':0
}

for item in sorted_distance_neighborhood:
    if k == 0:
        break
    answer[file.loc[item[0]]['К/Ч']]=answer[file.loc[item[0]]['К/Ч']]+1
    k-=1
if answer['Ч']>answer['К']:
    print('Ч')
else:
    print('К')
