import os
import json
import shutil

for directory in os.listdir("data"):
    for file_ in os.listdir(os.path.join("data", directory)):
        if file_.endswith(".txt"):
            output_file = os.path.join("output", directory) + ".txt"
            output = open(output_file, 'a')
            output.write(open(os.path.join("data", directory, file_), 'r').read())
        elif file_.endswith(".json"):
            output_file = os.path.join("output", directory) + ".json"
            # load current json
            if os.path.exists(output_file):
                already_added = open(output_file, 'r').read()
                current_json = json.loads(already_added)

                # add new lists
                new_input = open(os.path.join("data", directory, file_), 'r').read()
                new_lists = json.loads(new_input)

                start_id = len(current_json) + 1
                for i in range(len(new_lists)):
                    new_lists[i]["id"] = start_id + i
                    current_json.append(new_lists[i])

                # write back to file
                with open(output_file, 'w') as already_added:
                    json.dump(current_json, already_added)
            else:
                shutil.copy(os.path.join("data", directory, file_), output_file)



