# TranX User Study Raw Dataset and Data Analysis

The user identification information has been anonymized.
A total of 7 categories from `task1` to `task7`.

Check out data in `data/` directory, some important source data files are:

- `users.csv`: All user information, their expertise in python, programming, task categories, etc.
- `completed_time.csv`: User and task as unique identifier.
- `plugin_query_counts.csv`: Number of plugin queries for each user/task, and number of queries selecting generation and retrieval results. Only has data for those that use plugin.
- `plugin_queries.csv`: Query strings with user and task.
- `browser_event_counts.csv`: Number of URL GETs for each user/task, and number of those that are "search queries". Available for all user/task.
- `post_task_survey.csv`: The results from the survey after each task completion. 
    - difficulty: How difficult did you feel the task was? (1: very easy to 5: very difficult)
    - performance: How would you evaluate your performance on the task? (1: very poor to 5: very good)
    - efficiency: Only exists when using plugin. How do you think the plugin impacted your efficiency timewise, if at all? (1: hindered significantly, to 3: neither hindered nor helped, to 5: helped significantly)
    - quality: Only exists when using plugin. How do you think the plugin impacted your quality of life, with respect to ease of coding, concentration, etc., if at all? (1: hindered significantly, to 3: neither hindered nor helped, to 5: helped significantly)",
    - help: How often did you need to look for help during the task outside of the plugin, including web search, looking up API references, etc.?  (1: not at all to 5: very often)
- `scores.csv`: Evaluated scores for each user/task. `category_experience` means the user's experience in the current task category, according to survey.

At the root directory, there are Python scripts for data analysis and plotting.
For the main analysis presented in the paper, please refer to the R Markdown notebook `tranx.Rmd`.

Task evaluation rubrics:
https://github.com/neulab/tranx-study/blob/master/rubrics.md
User submissions: `submissions/userid_task_timestamp/` directories. Only need to check `main.py` against the rubrics.
