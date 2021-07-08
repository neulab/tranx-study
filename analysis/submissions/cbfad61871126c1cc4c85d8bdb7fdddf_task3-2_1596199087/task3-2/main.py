import os
import json

dir_in = "data"
dir_out = "output"
cur_filename = ""
lines = []
json_data = []
json_data_cur = []
cur_id = 1
for root, dirs, files in os.walk(dir_in):
    for file in files:
        if os.path.basename(root) != cur_filename and cur_filename != "":
            if len(lines) != 0:
                with open(os.path.join(dir_out, cur_filename + ".txt"), "w+") as file_out:
                    file_out.writelines(lines)
            else:
                with open(os.path.join(dir_out, cur_filename + ".json"), "w+") as file_out:
                    json.dump(json_data, file_out)

            lines = []
            cur_id = 1
            json_data = []
            cur_filename = os.path.basename(root)

        cur_filename = os.path.basename(root)
        if file[-3::1] == "txt":
            with open(os.path.join(root, file), "r") as file_txt:
                lines.extend(file_txt.readlines())
        elif file[-4::1] == "json":
            with open(os.path.join(root, file), "r") as json_file:
                json_data_cur = json.load(json_file)
                for line in json_data_cur:
                    line_cur = line
                    line_cur["id"] = cur_id
                    json_data.append(line_cur)
                    cur_id += 1
