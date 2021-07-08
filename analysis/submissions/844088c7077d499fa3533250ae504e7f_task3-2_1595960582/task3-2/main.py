import os
import pathlib
import json

for (dirpath, dirnames, fnames) in os.walk('data/'):
    output_file = os.path.join('output/', *pathlib.Path(dirpath).relative_to('data/').parts)

    txt_file_content = ''
    for txt_file in sorted([fname for fname in fnames if fname.endswith('.txt')]):
        with open(os.path.join(dirpath, txt_file), 'r') as f:
            txt_file_content += f.read()

    if len(txt_file_content) > 0:
        with open(output_file + '.txt', 'w') as f:
            f.write(txt_file_content)

    json_content = []
    for json_file in sorted([fname for fname in fnames if fname.endswith('.json')]):
        with open(os.path.join(dirpath, json_file), 'r') as f:
            json_content.extend(json.loads(f.read()))

    for i, elem in enumerate(json_content):
        json_content[i]['id'] = i + 1

    if len(json_content) > 0:
        with open(output_file + '.json', 'w') as f:
            f.write(json.dumps(json_content))
