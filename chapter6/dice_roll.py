import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import random

rolls = [random.randrange(1, 3) for i in range(20000)]#tossing a coin 1 = 'heads' 2 = 'tails
values, frequencies = np.unique(rolls, return_counts = True)

sns.set_style('whitegrid')
axes = sns.barplot(x=values, y=frequencies, palette='bright')

title = f'Coin Tossing {len(rolls):,} times'
axes.set_title(title)
axes.set(xlabel='Coin Value', ylabel='Frequency')

# make some space for text above the bar top
axes.set_ylim(top = max(frequencies) * 1.10)

# show frequency and % for each bar
for bar, frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width() / 2.0
    text_y = bar.get_height()
    text = f'{frequency:,}\n{frequency / len(rolls):.3%}'
    axes.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom')

plt.show()