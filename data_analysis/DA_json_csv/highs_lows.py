import csv

from datetime import datetime
from matplotlib import pyplot as plt


# Чтение максимальных температур из файла
# filename = 'sitka_weather_07-2014.csv'
# filename = 'sitka_weather_2014.csv'
filename = 'death_valley_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Чтение дат
    dates, highs, lows = [], [], []

    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
        # current_date = datetime.strptime(row[0], "%Y-%m-%d")
        # dates.append(current_date)
        #
        # high = int(row[1])
        # highs.append(high)
        #
        # low = int(row[3])
        # lows.append(low)

    # print(header_row)
    # # нумерація загаловка
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    # highs = [int(row[1]) for row in reader]
    # print(highs)

    # Нанесение данных на диаграмму.
    fig = plt.figure(dpi=100, figsize=(10, 6))
    # plt.plot(dates, highs, c='red')
    # plt.plot(dates, lows, c='blue')
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    # Форматирование диаграммы
    # plt.title("Daily high temperatures, July 2014", fontsize=24)
    # plt.xlabel('', fontsize=16)
    # plt.title("Daily high temperatures - 2014", fontsize=14)
    # plt.title("Daily high and low temperatures - 2014", fontsize=24)

    title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
    plt.title(title, fontsize=20)
    plt.xlabel('', fontsize=12)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=14)
    plt.tick_params(axis='both', which='major', labelsize=12)

    plt.show()