import editdistance
import nltk
import pandas as pd
from utils import get_completed_user_tasks, db
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

matplotlib.rcParams.update({'font.size': 14})


def get_plugin_edits():
    collection = db['events']
    completed = get_completed_user_tasks()
    data = []
    all_queries = {}
    edit_dists = []
    for item in completed:
        user_id, task = item['userid'], item['task']

        for record in collection.find({'userId': user_id,
                                       'projectName': task}):
            if record['eventType'] == 'query':
                query = record['query']
                hashcode = record['hash']
                selected_idx = record['selectedIndex']
                selected_candidate = record['candidates'][selected_idx]['value']
                if selected_idx < 7:
                    generation = 1
                else:
                    generation = 0
                all_queries[hashcode] = {'selected_candidate': selected_candidate,
                                         'is_generation': generation,
                                         'query': query}

            if record['eventType'] == 'edit':
                final_code = record['finalModifiedCode']
                final_code_tokens = nltk.word_tokenize(final_code)

                original_code = all_queries[record['hash']]['selected_candidate']
                original_code_tokens = nltk.word_tokenize(original_code)
                edit_dists.append({'edit_dist': editdistance.eval(original_code_tokens, final_code_tokens),
                                   'original_len': len(original_code_tokens),
                                   'final_len': len(final_code_tokens),
                                   'is_generated': all_queries[record['hash']]['is_generation']})
    return edit_dists


if __name__ == '__main__':
    # edit_dists = get_plugin_edits()
    # df = pd.DataFrame(edit_dists)
    # df.to_csv('data/edit_dists.csv')
    df = pd.read_csv('data/edit_dists.csv')
    df['percentage_to_original'] = df['edit_dist'] / df['original_len']
    print(df.columns)
    df = df.rename(columns={'edit_dist': 'Edit Distance',
                            'original_len': 'Original Length',
                            'final_len': 'Final Length'})
    df = pd.melt(df, id_vars=['is_generated'], value_vars=['Original Length', 'Final Length', 'Edit Distance'],
                 value_name='tokens')

    df.loc[(df.is_generated == 0), 'is_generated'] = 'Retrieved'
    df.loc[(df.is_generated == 1), 'is_generated'] = 'Generated'

    print(df)
    ax = sns.violinplot(x="variable", y="tokens", hue="is_generated",
                        data=df, palette="muted", cut=0, inner='quartile', split=True)
    sns.despine()
    ax.set(ylim=(-10, 150))
    ax.legend(loc='upper right', frameon=False)
    plt.xlabel("")
    ax.set(ylabel='Tokens')
    plt.savefig('figures/dist_violin.pdf')
