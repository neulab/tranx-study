# Example code, write your program here
import sys
import requests

if sys.argv[1] == 'read_user_posts':
    user_id = sys.argv[2]
    if user_id.isnumeric():
        if user_id <= '10':
            req = requests.get('https://jsonplaceholder.typicode.com/posts?userId='+user_id)
            print(req.text)
        else:
            print("No results found!")
    else:
        print("Arguments Error!")
elif sys.argv[1] == 'read_posts_comments':
    post_id =sys.argv[2]
    if post_id.isnumeric() :
        if post_id <= '100':
            req = requests.get('https://jsonplaceholder.typicode.com/posts/' + post_id+'/comments')
            print(req.text)
        else :
            print("No results found!")
    else:
        print("Arguments Error!")
elif sys.argv[1] == 'read_user_posts_comments':
    user_id = sys.argv[2]
    if user_id.isnumeric():
        if user_id <= '10':
            begin = ((int(user_id)-1)*10)+1
            ending = (int(user_id)*10)+1
            for i in range (begin,ending):
                post = requests.get('https://jsonplaceholder.typicode.com/posts/' + str(i))
                comment =  requests.get('https://jsonplaceholder.typicode.com/posts/' + str(i) + '/comments')
                print(post.text)
                print(comment.text)
        else:
            print("No results found!")
    else:
        print("Arguments Error!")
else:
    print("Arguments Error!")