from die import Die
import pygal

# Создание кубика D6.
die_1 = Die()
die_2 = Die()

# Моделирование серии бросков с сохранением результатов в списке.

# results = []
#
# # for roll_num in range(100):
# for roll_num in range(1000):
#
# #     result = die.roll()
#     result = die_1.roll() + die_2.roll()
#     results.append(result)

results = [(die_1.roll() + die_2.roll()) for roll_num in range(1000)]

# print(results)

# Анализ результатов.
#frequencies = []
max_result = die_1.num_sides + die_2.num_sides
# for value in range(2, max_result+1):
# # for value in range(1, die.num_sides+1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

#
frequencies = [value for value in range(2, max_result+1)]
# print(frequencies)

# Визуализация результатов.
hist = pygal.Bar()

# hist.title = "Results of rolling one D6 1000 times."
# hist.x_labels = ['1', '2', '3', '4', '5', '6']

hist.title = "Results of rolling two D6 dice 1000 times."
# hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

hist.x_labels = [str(x) for x in range(2, max_result+1)]
# print(hist.x_labels)

hist.x_title = "Result"
hist.y_title = "Frequency of Result"

# hist.add('D6', frequencies)
hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')
