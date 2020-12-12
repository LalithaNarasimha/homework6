from matplotlib import animation
import matplotlib.pyplot as plt
import random
import seaborn as sns
import sys

NUMBER_OF_FRAMES = 600
ROLLS_PER_FRAME = 10

# this function is called by animation to render each frame
# the first argument frame_number is provided by animation
def update(frame_number, faces, frequencies):
    for _ in range(ROLLS_PER_FRAME):  # roll the dice for the specified times
        dice_key = random.randrange(1, 3) - 1
        frequencies[dice_key] += 1

    plt.cla() # clear old content
    axes = sns.barplot(x=faces, y=frequencies, palette='bright')
    total_rolls = sum(frequencies)
    title = f'Dice frequencies for {total_rolls:,} rolls'
    axes.set_title(title)
    axes.set(xlabel='Dice Value', ylabel='Frequency')

    # make some space for text above the bar top
    axes.set_ylim(top = max(frequencies) * 1.10)

    # show frequency and % for each bar
    for bar, frequency in zip(axes.patches, frequencies):
        text_x = bar.get_x() + bar.get_width() / 2.0
        text_y = bar.get_height()
        text = f'{frequency:,}\n{frequency / total_rolls:.3%}'
        axes.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom')

sns.set_style('whitegrid')
figure = plt.figure('Rolling a Sixe-sided Dice')
values = list(range(1, 3))
frequencies = [0] * 2

die_animation = animation.FuncAnimation(
    figure, update, repeat=False, frames=NUMBER_OF_FRAMES, interval=33,
    fargs=(values, frequencies)
)

plt.show()