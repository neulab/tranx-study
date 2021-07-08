# Example code, write your program here
import pandas as pd
import os
# ---- BEGIN AUTO-GENERATED CODE ----
# ---- yh0yy8pa5tyixsqc3tcra7w02 ----
# query: load csv data
# to remove these comments and send feedback press alt-G
data = pd.read_csv('data.csv', index_col = 0)
# ---- END AUTO-GENERATED CODE ----
data = data.iloc[:, :-1].set_index('first_name')
if not os.path.exists('output'): os.makedirs('output')
data.to_csv('output/output.csv')