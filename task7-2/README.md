# Task Description

You are expected to provide visualizations about the relationship between student gender and race/ethnicity group with respect to test scores using the student score data provided in `StudentsPerformance.csv` file. 

By running `python3 main.py`, draw a plot containing 3 subplots arranged horizontally, each describing math, reading and writing scores respectively and save it to `grouped_scores.png`. The whole plot is titled "Scores by race/ethnicity and gender", with a size of 20 inches wide and 6 inches high.

For each subplot, create a grouped bar chart subtitled "Math", "Reading", and "Writing".
Specifically, the x-axis should be labeled "Race/Ethnicity", with ticks showing the group name `A, B, C, ...` as per data file.
The y-axis should be the average score for the subject, titled "Average Scores".
For each race/ethnicity group, draw two bars representing two genders, marked in legend as "Male" and "Female".
The average scores (2 decimals) should be shown on top of the bars.
The bar width should be 0.35 inches.

# Example Output

```
$ python3 main.py
$ ls .
grouped_scores.png ...

```

You can also check out directory `example_output/`.
