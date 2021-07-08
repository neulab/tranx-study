# Example code, write your program here
import requests, sys, json

if len(sys.argv) < 3:
    print ("Arguments error")
    sys.exit(1)
#Check for read_user_posts <userid>
if sys.argv[1] == 'read_user_posts' and (int (sys.argv[2]) > 0 and int (sys.argv[2]) < 11):
    #Do some stuff
    requestValue = "https://jsonplaceholder.typicode.com/posts?userId=" + sys.argv[2]
    req = requests.get(requestValue)
    jsonData = json.loads(req.content.decode())
#    print(jsonData)
    print ("Posts of user " + sys.argv[2] + ':')
    counter = 1
    for entry in jsonData:
#        print (entry['userId'])
        if (entry['userId'] == int(sys.argv[2])):
            print("Post %s/10" %counter)
            counter+=1
            print("ID: %s" %entry['id'])
            print("Title: " + entry['title'])
            print("Body: " + entry['body'])
            print('')

#Check for read_post_comments <postid>
elif sys.argv[1] == "read_post_comments" and (int (sys.argv[2]) > 0 and int (sys.argv[2]) < 101):
    #Do some stuff
    print("Second case")
    requestValue = "https://jsonplaceholder.typicode.com/posts/" + sys.argv[2] + '/comments'
    req = requests.get(requestValue)
    jsonData = json.loads(req.content.decode())
#    print(jsonData)
    print ("Comments of post " + sys.argv[2] + ':')
    counter = 1
    for entry in jsonData:
#        print (entry['userId'])
        if (entry['postId'] == int(sys.argv[2])):
            print("Comment %s/5" %counter)
            counter+=1
            print("Name: " + entry['name'])
            print("Email: " + entry['email'])
            print("Body: " + entry['body'])
            print('')

#Check for read_user_posts_comments <userid>
elif sys.argv[1] == "read_user_posts_comments" and (int (sys.argv[2]) > 0 and int (sys.argv[2]) < 11):
    #Do some stuff
    print("Third case")
    requestValue = "https://jsonplaceholder.typicode.com/posts?userId=" + sys.argv[2]
    req = requests.get(requestValue)
    jsonData = json.loads(req.content.decode())
    #    print(jsonData)
    print("Posts of user " + sys.argv[2] + ':')
    counter = 1
    for entry in jsonData:
        #        print (entry['userId'])
        if (entry['userId'] == int(sys.argv[2])):
            print("Post %s/10" % counter)
            counter += 1
            print("ID: %s" % entry['id'])
            print("Title: " + entry['title'])
            print("Body: " + entry['body'])
            commentRequestValue = "https://jsonplaceholder.typicode.com/posts/" + str(entry['id']) + '/comments'
            comReq = requests.get(commentRequestValue)
            jsonData_comment = json.loads(comReq.content.decode())
#            print(jsonData_comment)
            counter_Comments = 1
            for entry_comments in jsonData_comment:
                #        print (entry['userId'])
                print("\tComment %s/5" % counter_Comments)
                counter_Comments += 1
                print("\tName: " + entry_comments['name'])
                print("\tEmail: " + entry_comments['email'])
                print("\tBody: " + entry_comments['body'])
                print('')
            print('')

else:
    print ("No results found")