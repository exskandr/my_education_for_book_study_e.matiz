from die import Die

import pygal

# Create a D6 and a D10.
die_1 = Die(8)
die_2 = Die(8)

# Make some rolls, and store results in a list.
results = [(die_1.roll() + die_2.roll()) for roll_num in range(50000)]

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling a D8 and a D8 50,000 times."
hist.x_labels = [str(x) for x in range(2, max_result + 1)]

hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D8 + D8', frequencies)
hist.render_to_file('dice_d8_visual.svg')
