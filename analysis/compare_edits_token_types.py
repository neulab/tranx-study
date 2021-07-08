import string
from collections import Counter

import csv
from io import BytesIO

import editdistance
import json
import nltk
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import tokenize

matplotlib.rcParams.update({'font.size': 14})


def tokenize_tags(source):
    g = tokenize.tokenize(BytesIO(source.encode('utf-8')).readline)
    tags = []
    parse_error = False
    try:
        for toknum, tokval, _, _, _ in g:
            tags.append(tokenize.tok_name[toknum])
    except:
        parse_error = True
    return tags, parse_error


if __name__ == '__main__':
    # collection = db['events']
    # completed = get_completed_user_tasks()
    # data = []
    # all_queries = {}
    # before_and_after = []
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
    #             original_code = all_queries[record['hash']]['selected_candidate']
    #             before_and_after.append((original_code, final_code, all_queries[record['hash']]['is_generation']))
    #
    # with open('data/before_and_after.json', 'w') as before_and_after_file:
    #     json.dump(before_and_after, before_and_after_file)
    # exit()
    before_and_after = json.load(open('data/before_and_after.json', encoding='utf-8'))
    before_tags = []
    after_tags = []
    parse_error_count = 0
    for row in before_and_after:
        before, before_error = tokenize_tags(row[0])
        after, after_error = tokenize_tags(row[1])
        if not before_error and not after_error:
            before_tags.extend(before)
            after_tags.extend(after)
        else:
            parse_error_count += 1

    before_freq = Counter(before_tags)

    after_freq = Counter(after_tags)

    before_total = sum(before_freq.values(), 0.0)
    print(before_total)
    for key in before_freq:
        before_freq[key] /= before_total

    after_total = sum(after_freq.values(), 0.0)
    print(after_total)
    for key in after_freq:
        after_freq[key] /= after_total

    print(parse_error_count)
    after_freq.subtract(before_freq)
    for item in after_freq.most_common():
        print(item[0], item[1])
