#Open data file and copy the contents
with open('data.csv', 'r') as dr:
    d_contents = dr.readlines()

#Create output file
with open('output.csv', 'w') as dw:
#Split the details of each person into a list and then write to file
    for person in d_contents:
        info = person.split(',')
        output = info[1:5]
        i = 0
        for element in output:
            if i <= 2:
                dw.write(element + ',')
            else:
                dw.write(element)
            i += 1
        dw.write("\n")


