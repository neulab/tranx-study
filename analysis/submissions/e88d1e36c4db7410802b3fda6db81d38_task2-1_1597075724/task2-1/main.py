# Example code, write your program here
# import pandas as pd
# df = pd.read_csv('data.csv',header=None)
# print(df)
import pandas as pd
f = pd.read_csv("data.csv")
keep_col = ['first_name','last_name','email','gender']
new_f = f[keep_col]
new_f.to_csv("output/output.csv", index=False)

# f = pd.read_csv("output/output.csv")
# print(f)


