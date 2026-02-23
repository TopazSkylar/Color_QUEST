import csv
import random

from Tools.scripts.summarize_stats import print_title

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