# модуль для хранения функций
from datetime import timedelta
from random import sample


def get_songs(songs: list|dict) -> dict[str, float]:
    """Функция формирует словари трех случайных песен с помощью модуля random"""
    three_songs_dict = {}
    # оператор match-case — операции по шаблону 
    match songs:
        case list():
            for song in sample(songs, k=3):
                three_songs_dict[song[0]] = song[1]
    
        case dict():
            for song, dur in sample(sorted(songs.items()), k=3):
                three_songs_dict[song] = dur
    
    return three_songs_dict


def time_counter(dct: dict[str, float]) -> timedelta:
    """Функция суммирует время из словаря с помощью модуля datetime"""
    total_dur = timedelta()
    for k in dct:
        minutes, seconds = str(dct[k]).split(".")
        total_dur += timedelta(minutes=int(minutes), seconds=int(seconds))
    
    return total_dur 
