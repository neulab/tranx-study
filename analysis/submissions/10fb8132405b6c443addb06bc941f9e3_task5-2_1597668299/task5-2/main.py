import requests
import sys


if sys.argv[1] == 'read_user_posts':
    user_id = sys.argv[2]
    r = requests.get('https://jsonplaceholder.typicode.com/posts?userId=' + user_id)
    print(r.text)

elif sys.argv[1] == 'read_post_comments':
    post_id = sys.argv[2]
    r = requests.get('https://jsonplaceholder.typicode.com/posts/' + post_id + '/comments')
    print(r.text)

elif sys.argv[1] == 'read_user_posts_comments':
    userr_id = sys.argv[2]
    x = ((int(userr_id)-1)*10) + 1
    y = int(userr_id)*10

    for i in range(x,y+1):
        posts = requests.get('https://jsonplaceholder.typicode.com/posts/' + str(i))
        comments = requests.get('https://jsonplaceholder.typicode.com/posts/' + str(i) + '/comments')
        print(posts.text)
        print(comments.text)

else:
    print("Arguments Error!")