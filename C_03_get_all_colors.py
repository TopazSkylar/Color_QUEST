import csv
import random

def round_ans(val):
    """
    Rounds numbers to nearest integer
    number to rounded.
    rounded number (an integer)
    """
    var_rounded = (val * 2 + 1) // 2
    raw_rounded = "{:.0f}".format(var_rounded)
    return int(raw_rounded)


# Retrieve colors from csv file and put them in a list
file = open("00_colour_list_hex_v3.csv", "r")
all_colors = list(csv.reader(file, delimiter=","))
file.close()

# remove the first row
all_colors.pop(0)

round_colors = []
color_scores = []

# loop until we have four colors with different scores...
while len(round_colors) < 4:
    potential_color = random.choice(all_colors)

    # Get the score and check it's not a duplicate
    if potential_color[1] not in color_scores:
        round_colors.append(potential_color)
        color_scores.append(potential_color[1])

print(round_colors)
print(color_scores)

# find target score (median)

# change scores to integers
int_scores = [int(x) for x in color_scores]
int_scores.sort()

median = (int_scores[1] + int_scores[2]) / 2
median = round_ans(median)
print("median", median)