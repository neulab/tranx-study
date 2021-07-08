import string
from collections import Counter

import editdistance
import nltk
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

matplotlib.rcParams.update({'font.size': 14})

if __name__ == '__main__':
    # collection = db['events']
    # completed = get_completed_user_tasks()
    # data = []
    # all_queries = {}
    # edit_dists = []
    # before_tokens = []
    # after_tokens = []
    # for item in completed:
    #     user_id, task = item['userid'], item['task']
    #
    #     for record in collection.find({'userId': user_id,
    #                                    'projectName': task}):
    #         if record['eventType'] == 'query':
    #             query = record['query']
    #             hashcode = record['hash']
    #             selected_idx = record['selectedIndex']
    #             selected_candidate = record['candidates'][selected_idx]['value']
    #             if selected_idx < 7:
    #                 generation = 1
    #             else:
    #                 generation = 0
    #             all_queries[hashcode] = {'selected_candidate': selected_candidate,
    #                                      'is_generation': generation,
    #                                      'query': query}
    #
    #         if record['eventType'] == 'edit':
    #             final_code = record['finalModifiedCode']
    #             final_code_tokens = nltk.word_tokenize(final_code)
    #
    #             original_code = all_queries[record['hash']]['selected_candidate']
    #             original_code_tokens = nltk.word_tokenize(original_code)
    #             before_tokens.extend(original_code_tokens)
    #             after_tokens.extend(final_code_tokens)
    #
    # with open('data/before_tokens.txt', 'w') as before_file:
    #     before_file.write("\n".join(before_tokens))
    # with open('data/after_tokens.txt', 'w') as after_file:
    #     after_file.write("\n".join(after_tokens))

    before_tokens = open('data/before_tokens.txt').read().split('\n')
    after_tokens = open('data/after_tokens.txt').read().split('\n')
    exclude = set(string.punctuation)
    before_tokens = [tok for tok in before_tokens if tok not in exclude]
    after_tokens = [tok for tok in after_tokens if tok not in exclude]

    before_freq = Counter(before_tokens)

    after_freq = Counter(after_tokens)

    before_total = sum(before_freq.values(), 0.0)
    print(before_total)
    for key in before_freq:
        before_freq[key] /= before_total

    after_total = sum(after_freq.values(), 0.0)
    print(after_total)
    for key in after_freq:
        after_freq[key] /= after_total

    after_freq.subtract(before_freq)
    print(after_freq.most_common(20))

    print(after_freq.most_common()[:-20-1:-1])