import csv
import json

with open('data/conala-corpus/conala-train.json') as f:
    conala_train = json.loads(f.read())

chosen = {}

with open('data/candidate_lengths.csv') as f:
    reader = csv.reader(f)
    _header = next(reader)
    for row in reader:
        [row_id, is_generation, query, snippet_len, snippet] = row
        chosen[(query.strip(), snippet_len, snippet)] = True

interesting_queries = {}
all_queries = {}

with open('data/all_candidate_lengths_gr.csv', 'w') as g:
    writer = csv.writer(g)
    writer.writerow(['row_id', 'query', 'is_chosen', 'is_generation', 'snippet_len', 'snippet'])
    with open('data/all_candidate_lengths.csv') as f:
        reader = csv.reader(f)
        _header = next(reader)
        for row in reader:
            [row_id, is_generation, query, snippet_len, snippet] = row
            all_queries[query.strip()] = True
            is_chosen = chosen.get((query.strip(), snippet_len, snippet), False)
            # is_generation = (int(row_id) % 14) < 7
            writer.writerow([row_id, query.strip(), is_chosen, bool(int(is_generation)), snippet_len, snippet])

            if is_chosen and bool(int(is_generation)):
                interesting_queries[query.strip()] = snippet


retrieval_snippets = {}

with open('data/all_candidate_lengths_gr_interesting.csv', 'w') as g:
    writer = csv.writer(g)
    with open('data/all_candidate_lengths_gr.csv') as f:
        reader = csv.reader(f)
        _header = next(reader)
        writer.writerow(_header)
        for row in reader:
            [row_id, query, is_chosen, is_generation, snippet_len, snippet] = row
            if query in interesting_queries:
                # print (('Here', str(int(is_generation))))
                if is_generation == 'False':
                    retrieval_snippets.setdefault(query, set([]))
                    retrieval_snippets[query].add(snippet)
                writer.writerow(row)

# print (retrieval_snippets)

num_interesting = 0
num_matches = 0
num_conala_matches = 0
num_conala_exact_matches = 0

for query in interesting_queries.keys():
    num_interesting += 1
    gen_snippet = interesting_queries[query]
    print ('\n###########')
    print ('QUERY:' + query)
    print ('\nGENERATED (& CHOSEN) SNIPPET:\n' + gen_snippet)
    # print ((query, gen_snippet))
    # print (retrieval_snippets.get(query, set([])))
    match = 0
    for retrieval_snippet in retrieval_snippets[query]:
        print ('\nSNIPPET:\n' + retrieval_snippet)
        if retrieval_snippet.find(gen_snippet) > -1:
            print ('\nMATCH:\n' + retrieval_snippet)
            match = 1
    if match:
        num_matches += 1

    conala_match = 0
    conala_exact_match = 0
    for conala_snippet in [e['snippet'] for e in conala_train]:
        # print ('\nSNIPPET:\n' + retrieval_snippet)
        if gen_snippet.find(conala_snippet) > -1:
            print ('\nCONALA MATCH:\n' + conala_snippet)
            conala_match = 1
        if gen_snippet == conala_snippet:
            print ('\nCONALA EXACT MATCH:\n' + conala_snippet)
            conala_exact_match = 1
    if conala_match:
        num_conala_matches += 1
    if conala_exact_match:
        num_conala_exact_matches += 1
    # print ('ANY MATCH:' + str(match))

print ('\n###########')
print ('NUM UNIQUE QUERY-SNIPPET PAIRS IN candidate_lengths.csv:' + str(len(chosen.keys())))
print ('NUM UNIQUE QUERIES IN candidate_lengths.csv: ' + str(len(set([query.strip() for (query, snippet_len, snippet) in chosen.keys()]))))
print ('NUM QUERIES:' + str(len(all_queries.keys())))
print ('NUM INTERESTING:' + str(len(interesting_queries.keys())))
# print ('NUM INTERESTING:' + str(num_interesting))
print ('NUM MATCHES:' + str(num_matches))
print ('CONALA TRAIN:' + str(len(conala_train)))
print ('NUM CONALA MATCHES:' + str(num_conala_matches))
print ('NUM CONALA EXACT MATCHES:' + str(num_conala_exact_matches))
