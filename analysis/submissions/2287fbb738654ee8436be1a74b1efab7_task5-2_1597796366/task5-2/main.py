# Example code, write your program here

import requests
import sys

if sys.argv[1] == 'read_user_posts':
    user_id = sys.argv[2]
    r = requests.get('https://jsonplaceholder.typicode.com/posts?userId='+user_id)
    print(r.text)
elif sys.argv[1] =='read_post_comments':
    post_id = sys.argv[2]
    r = requests.get('https://jsonplaceholder.typicode.com/post/'+post_id+'/comments')
elif sys.argv[1] == 'read_user_posts_comments':
    user_id = sys.argv[2]
    x = ((int(user_id)-1)*10)+1
    y = int(user_id)*10

    for i in range(x,y+1):
        post = requests.get('https://jsonplaceholder.typicode.com/post/'+str(i))
        user = requests.get('https://jsonplaceholder.typicode.com/post/'+str(i)+'/comments')
        print(post.text)
        print(user.text)

else:
    print('Arguments Error!')