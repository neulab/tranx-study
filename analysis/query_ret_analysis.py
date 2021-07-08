import csv

all_compliant_queries = []
with open('data/plugin_queries.csv', encoding='utf-8') as qf:
    reader = csv.reader(qf,)
    for row in reader:
        query = row[3]
        if '`' in query or '"' in query:
            all_compliant_queries.append(query)

with open('data/compliant_queries.csv', 'w', encoding='utf-8') as outfile:
    outfile.write('\n'.join(all_compliant_queries))
