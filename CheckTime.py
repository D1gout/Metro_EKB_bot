from datetime import datetime

from TimeList import TimeList


def CheckTime(station_time):
    hours = datetime.now().hour
    hours_next = datetime.now().hour + 1
    minutes = datetime.now().minute + 1

    if hours_next == 24:
        hours_next = 0

    if hours == 24:
        hours = 0

    if hours > int(station_time[len(station_time) - 1].split(':')[0]) and \
            minutes > int(station_time[len(station_time) - 1].split(':')[1]):
        return "Метро закрыто"

    for i in range(len(station_time)):

        if hours == int(station_time[i].split(':')[0]):

            if hours_next == int(station_time[i + 1].split(':')[0]):
                next_time = 60 - minutes + int(station_time[i + 1].split(':')[1])
            else:
                next_time = int(station_time[i + 1].split(':')[1]) - minutes

            if minutes < int(station_time[i].split(':')[1]):
                time = int(station_time[i].split(':')[1]) - minutes

                return f"Поезд прибудет через {time} мин.\nСледующий через {next_time} мин."

            elif minutes == int(station_time[i].split(':')[1]):

                return f"Поезд прибыл\nСледующий через {next_time} мин."

        if hours_next == int(station_time[i].split(':')[0]):
            time = 60 - minutes + int(station_time[i].split(':')[1])
            next_time = 60 - minutes + int(station_time[i + 1].split(':')[1])
            return f"Поезд прибудет через {time} мин.\nСледующий через {next_time} мин."
