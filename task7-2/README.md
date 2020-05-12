# Task Description

You are expected to provide visualizations about the relationship between student gender and race/ethnicity group with respect to test scores using the student score data provided in `StudentsPerformance.csv` file. 

By running `python main.py`, draw a plot containing 3 subplots arranged horizontally, each describing math, reading and writing scores respectively and save it to `grouped_scores.png` with automatic size and coloring. The whole plot is titled "Scores by race/ethnicity and gender"

For each subplot, create a grouped bar chart subtitled "Math", "Reading", or "Writing".
Specifically, the x-axis should be the race/ethnicity, represented in `A, B, C, ...` as per data file.
The y-axis should be the average score for the subject, titled "Average Scores".
For each race/ethnicity group, draw two bars representing two genders, marked in legend as "Men" and "Women".
The average scores should be shown on top of the bars.

Each of the 3 subplot looks similar to the following example:
![](https://matplotlib.org/3.1.1/_images/sphx_glr_barchart_001.png)


# Example Output

```
$ python main.py
$ ls .
grouped_scores.png ...

```