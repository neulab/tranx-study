import sys
import requests

def print_comment(comments):
    no_comments = len(comments)
    for i in range(no_comments):
        comment = comments[i]
        print('\tComment %d/%d:' % (i + 1, no_comments))
        print('\tName: %s' % comment['name'])
        print('\tEmail: %s' % comment['email'])
        print('\tBody: %s\n' % comment['body'].replace('\n', '\n\t'))


def main():
    if sys.argv[1] == "read_user_posts":
        user_id = sys.argv[2]
        r = requests.get('https://jsonplaceholder.typicode.com/posts', params={'userId':user_id})
        posts = r.json()
        no_posts = len(posts)
        print('Posts of user %s:\n' % user_id)
        for i in range(no_posts):
            post = posts[i]
            print('Post %d/%d:' % (i+1, no_posts))
            print('ID: %s' % post['id'])
            print('Title: %s' % post['title'])
            print('Body: %s\n' % post['body'])
    elif sys.argv[1] == "read_post_comments":
        #GET /comments?postId=1
        post_id = sys.argv[2]
        r = requests.get('https://jsonplaceholder.typicode.com/comments', params={'postId':post_id})
        comments = r.json()
        no_comments = len(comments)
        print('Comments of post %s:\n' % post_id)
        for i in range(no_comments):
            comment = comments[i]
            print('Comment %d/%d:' % (i+1, no_comments))
            print('Name: %s' % comment['name'])
            print('Email: %s' % comment['email'])
            print('Body: %s\n' % comment['body'])

    elif sys.argv[1] == "read_user_posts_comments":
        user_id = sys.argv[2]
        r = requests.get('https://jsonplaceholder.typicode.com/posts', params={'userId':user_id})
        posts = r.json()
        no_posts = len(posts)
        print('Posts of user %s:' % user_id)
        for i in range(no_posts):
            post = posts[i]
            print('\nPost %d/%d:' % (i+1, no_posts))
            print('ID: %s' % post['id'])
            print('Title: %s' % post['title'])
            print('Body: %s' % post['body'])
            # get comments for each post
            r1 = requests.get('https://jsonplaceholder.typicode.com/comments', params={'postId': post['id']})
            print_comment(r1.json())
    else:
        print("Arguments error!")
        sys.exit()


if __name__ == "__main__":
    main()
