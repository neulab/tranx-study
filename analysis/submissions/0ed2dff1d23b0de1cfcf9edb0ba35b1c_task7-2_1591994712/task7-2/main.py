# Example code, write your program here
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def main():
    df = pd.read_csv("StudentsPerformance.csv")
    grouped = df.groupby(['gender', 'race/ethnicity'])
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(20, 6))
    bar_width = 0.35
    for ax, subject in zip(axes, ['math', 'reading', 'writing']):
        avg_score = grouped[f"{subject} score"].mean()
        for key, shift in [('male', -0.5), ('female', 0.5)]:
            value = avg_score[key].to_list()
            shift *= bar_width
            ax.bar(np.arange(len(value)) + shift, value, width=bar_width, label=key.capitalize())
            for i, v in enumerate(value):
                ax.text(i + shift, v + 2, f"{v:.2f}", ha='center', va='center')
        ax.set_xlabel("Race/Ethnicity")
        ax.set_ylabel("Average Scores")
        ax.set_xticklabels([0] + [x.split()[1] for x in avg_score['male'].index.to_list()])
        ax.set_title(subject.capitalize())
        ax.legend(loc="upper left")

    fig.suptitle("Scores by race/ethnicity and gender")
    fig.savefig("output/grouped_scores.png")


if __name__ == '__main__':
    main()
