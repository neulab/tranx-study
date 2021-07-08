# Example code, write your program here
import os,re,json

def Folderator():
    for subdir, dirs, files in os.walk('./data/'):
        if files:
            # Sort text files then copy the text in the final file
            if files[0].endswith(".txt"):
                files = sorted(files)
                final_contents = ''
                for file in files:
                    dir_name = re.search(r'(.*\/)(.*)',subdir)
                    dir_name = './output/' + dir_name[2] + '.txt'
                    original_file = open(subdir+os.sep+file,"r")
                    new_file = open(dir_name, "w")
                    final_contents = final_contents +str(original_file.read())
                new_file.write(final_contents)
            elif files[0].endswith(".json"):
                # Sort the json files
                files = sorted(files)
                first_time = 0
                final_contents = []
                for file in files:
                    dir_name = re.search(r'(.*\/)(.*)', subdir)
                    dir_name = './output/' + dir_name[2] + '.json'
                    original_file = open(subdir + os.sep + file, "r")
                    new_file = open(dir_name, "w")
                    # Concat the files by acquiring the last id from the previous json file
                    # and adding that id to all ids of the new list
                    if first_time == 0:
                        contents = json.loads(original_file.read())
                        prev_id = int(contents[len(contents)-1]['id'])
                        first_time = 1
                    else:
                        contents = json.loads(original_file.read())
                        for i in range(len(contents)):
                            contents[i]['id'] += prev_id
                        prev_id = int(contents[len(contents) - 1]['id'])
                    final_contents = final_contents + contents
                new_file.write(str(final_contents))
    return

if __name__ == '__main__':
    Folderator()