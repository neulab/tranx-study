# Example code, write your program here
import json
#read files and put them in one text file
txtoutput = open ("/vagrant/task3-2/output/filelist.txt", "w")

def writeText(inputpath):
    file = open (inputpath, "rt")
    txtfiles = file.readlines()
    for line in txtfiles:
        txtoutput.write(line)
    txtoutput.write('\n')
    file.close()
######################################################
writeText("/vagrant/task3-2/data/filelist/1.txt")
writeText("/vagrant/task3-2/data/filelist/a.txt")
writeText("/vagrant/task3-2/data/filelist/zz.txt")
#########################################################

#read json files and write them in one json file

jsonOutput = open ("/vagrant/task3-2/output/roster.json", "w")
jsonOutput.write("[")
counter = 1
def writeJson(path):
    global counter
    file = open(path, "r")
    jsonFile = json.loads(file.read())
    for entry in jsonFile:
        entry['id'] = counter
        jsonOutput.write(json.dumps(entry))
        counter = counter + 1
        if (counter != 61):
            jsonOutput.write(',\n')
    file.close()

writeJson("/vagrant/task3-2/data/roster/2020.json")
writeJson("/vagrant/task3-2/data/roster/2021.json")
writeJson("/vagrant/task3-2/data/roster/2022.json")
jsonOutput.write(']')
jsonOutput.close()
# #update count
# jsonOutput = open ("/vagrant/task3-2/output/roster.json", "r+")
# outFile = json.load(jsonOutput)
# counter = 1
# for entry in outFile:
#     print (entry['id'])
#     entry['id'] = counter
#     print (entry['id'])
#     counter = counter + 1

