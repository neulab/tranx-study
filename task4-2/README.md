# Task Description

After running `python main.py`, the program stores the list of world countries and populations from the table "Sovereign states and dependencies by population" in the HTML page `https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population` into `output/populations.csv`, and download the countries' flag thumbnails into directory `output/images`, named by `<country_name>.png`.

Specifically, `populations.csv` contains two columns, `country` (name of the country/territory as shown in the table from the webpage, excluding footnote marks, parentheses, etc.) and `population` (number of population, without comma). 
The data is ordered by the population in descending order.

For country thumbnails, the image format should be `.png` and the filename should be same as the country name appeared in the `populations.csv`.


# Example Output

```
$ python main.py
$ ls output
populations.csv  images
$ ls output/images
China.png   India.png
...
$ less output/populations.csv
country,population
China,1402973960
India,1363153843
...

```

You can also check out directory `example_output/`.