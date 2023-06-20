from datetime import datetime


def CheckTime(station_time):
    for i in range(len(station_time)):
        if datetime.now().hour == int(station_time[i].split(':')[0]):
            if datetime.now().minute < int(station_time[i].split(':')[1]):
                time = int(station_time[i].split(':')[1]) - datetime.now().minute
                next_time = int(station_time[i+1].split(':')[1]) - datetime.now().minute
                return f"Поезд прибудет через {time} мин.\nСледующий через {next_time} мин."
            elif datetime.now().minute == int(station_time[i].split(':')[1]):
                next_time = int(station_time[i + 1].split(':')[1]) - datetime.now().minute
                return f"Поезд прибыл\nСледующий через {next_time} мин."
