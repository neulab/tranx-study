import csv
from math import ceil

table_head = '''\\begin{table}[t] \\centering 
  \\caption{Unique user queries to the NL2Code plugin, per task.} 
  \\label{tbl:queries} 
  \\footnotesize
  \\renewcommand{\\arraystretch}{0.8}
\\begin{tabular}{lP{6cm}P{6cm}}
\\toprule
'''

table_foot = '''
\\bottomrule
\\end{tabular} 
\\end{table}
'''

longtable_head = '''\\renewcommand*{\\arraystretch}{0.8}
\\begin{longtable}{lLL}
\\caption{Sampled user queries for the oracle analysis. Queries for
    which the user chose a snippet from the code 
    generation model are shown in boldface. $\\bullet$ denotes 
    queries ``good enough'' on their own; $\\circ$ denotes queries
    good enough given the rest of the source file as context; the
    former is a strict subset of the latter.} \\label{tbl:queries-sampled} \\\\
\\toprule
Task & Queries & \\\\
\\midrule
\\endfirsthead
\\caption[]{(continued)}\\\\
\\toprule
Task & Queries & \\\\
\\midrule
\\endhead
\\bottomrule
\\endfoot
'''

longtable_foot = '''
\\bottomrule
\\end{longtable}
'''

def first_lower(s):
    return (s[0].lower() + s[1:])

def pad(query):
    return ('& %s ' % query)
    # return ('& %s & \\\\\n' % query)

def escape(query):
    q = query
    q = q.replace('%', '\\%')
    q = q.replace('_', '$\_$')
    q = q.replace('`', '\\texttt{\`}')
    q = q.replace('\\n', '\\textbackslash n')
    # q = q.replace('\\', '\\\\')
    return (q)

def highlight(query):
    return ('\\textbf{%s}' % query)

def bullet(query):
    return ('%s $\\bullet\\circ$' % query)

def circ(query):
    return ('%s $\\circ$' % query)

def distribute(task, raw_queries, num_columns):
    end_row = ceil(len(raw_queries) / num_columns)
    rows = {}
    start_idx = 0
    for column in range(num_columns):
        start_idx = start_idx * column
        end_idx = start_idx + end_row
        for idx, query in enumerate(raw_queries[start_idx:end_idx]):
            # print ((idx, query))
            rows.setdefault(idx, '')
            rows[idx] += pad(escape(query))
        start_idx += end_row
    for idx in sorted(rows.keys()):
        rows[idx] += '\\\\\n'
    return (rows)

# Count the number of queries per user
# We exclude users who didn't use the plugin enough
query_counts = {}
with open('data/plugin_queries.csv') as f:
    reader = csv.reader(f)
    _header = next(reader)
    for row in reader:
        [row_id,user,task,query,is_generation] = row
        query_counts.setdefault(user,0)
        query_counts[user] += 1

# Sanity check
min_plugin_uses = 4
print (len([c for c in query_counts.values() if c >= min_plugin_uses]))

# Read in the user queries
queries = {}
generation_queries = 0
with open('data/queries_sampled.csv') as f:
    reader = csv.reader(f)
    _header = next(reader)
    for row in reader:
        [row_id,user,task,query,good,good_with_context,is_generation] = row
        if query_counts[user] >= min_plugin_uses:
            queries.setdefault(task,set([]))
            q = first_lower(query.strip())
            if good == '1':
                q = bullet(q)
            elif good_with_context == '1':
                q = circ(q)
            if is_generation == '1':
                q = highlight(q)
                generation_queries += 1
            queries[task].add(q)
        else:
            print (row)

# Sanity check
print (str(sum([len(queries[task]) for task in queries.keys()])) + ' total queries')
print (str(generation_queries) + ' generation queries')

# exit()

# Output unique queries as LaTeX table
with open('table_queries_sampled.tex', 'w') as o:
    o.write(longtable_head)
    for task in sorted(queries.keys()):
        raw_queries = sorted(queries[task], key=lambda e:e.lower())
        rows = distribute(task, raw_queries, 2)
        for row_num in sorted(rows.keys()):
            if row_num == 0:
                o.write(task.replace('task','T') + ' ' + rows[row_num])
            else:
                o.write(rows[row_num])
    o.write(longtable_foot)

