# Example code, write your program here

import requests
import json
import sys


URL = 'https://jsonplaceholder.typicode.com'


def read_user_posts(userid):
    r = requests.get(URL + '/posts', params={'userId': userid})
    a = json.loads(r.content)
    if not len(a):
        print('No results found!')
        return
    print('Posts of user {u}'.format(u=userid))
    print('')
    for i in range(len(a)):
        aa = a[i]
        print('Post {i}/{t}'.format(i=i+1, t=len(a)))
        print('ID: {}'.format(aa['id']))
        print('Title: {}'.format(aa['title']))
        print('Body: {}'.format(aa['body']))
        print('')


def read_post_comments(postid, prefix=''):
    r = requests.get(URL + '/comments', params={'postId': postid})
    a = json.loads(r.content)
    if not len(a):
        print('No results found!')
        return
    print('Comments of post {u}'.format(u=len(a)))
    print('')
    for i in range(len(a)):
        aa = a[i]
        print('{p}Comment {i}/{t}'.format(p=prefix, i=i+1, t=len(a)))
        print('{p}Name: {c}'.format(p=prefix, c=aa['name']))
        print('{p}Email: {c}'.format(p=prefix, c=aa['email']))
        print('{p}Body: {c}'.format(p=prefix, c=aa['body']))
        print('')


def read_user_posts_comments(userid):
    r = requests.get(URL + '/posts', params={'userId': userid})
    a = json.loads(r.content)
    if not len(a):
        print('No results found!')
        return
    print('Posts of user {u}'.format(u=userid))
    for i in range(len(a)):
        aa = a[i]
        read_post_comments(aa['id'], prefix='    ')


router = {
    'read_user_posts': read_user_posts,
    'read_post_comments': read_post_comments,
    'read_user_posts_comments': read_user_posts_comments,
}

def main(argv):
    if 3 > len(argv):
        print('Arguments Error!')
        return
    if argv[1] not in router:
        print('Arguments Error!')
        return
    router[argv[1]](argv[2])

if __name__ == '__main__':
    main(sys.argv)
