# Импорты должны быть в начале
from functions import get_songs, time_counter

# Данные
my_favorite_songs = [
['Waste a Moment', 3.03],
['New Salvation', 4.02],
['Staying\' Alive', 3.40],
['Out of Touch', 3.03],
['A Sorta Fairytale', 5.28],
['Easy', 4.15],
['Beautiful Day', 4.04],
['Nowhere to Run', 2.58],
['In This World', 4.02],
]

my_favorite_songs_dict = {
'Waste a Moment': 3.03,
'New Salvation': 4.02,
'Staying\' Alive': 3.40,
'Out of Touch': 3.03,
'A Sorta Fairytale': 5.28,
'Easy': 4.15,
'Beautiful Day': 4.04,
'Nowhere to Run': 2.58,
'In This World': 4.02,
}

# функция запуска
def start():
    print(
        "Время звучаения трех случайных песен",
        f"для list - {time_counter(get_songs(my_favorite_songs))}", 
        f"для dict - {time_counter(get_songs(my_favorite_songs_dict))}", 
        sep="\n"
    )

# инициализационный скрипт
if __name__ == "__main__":
    start()



#############################################################
# Импорты. Зачем?
# Модуль это файл с расширением py
# Модуль бывают: самописные, встроенные, внешние

# импорт самописных модулей
# import functions
# import functions as f
# from functions import func

# func()

# импорт встроенных модулей
# import random

# print(random.choices([1, 2, 3, 4, 5], k=2))

# Как работает время из datetime?
# print(time(hour=13, minute=20, second=10)) # 13:20:10
