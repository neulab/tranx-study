# Example code, write your program here
import json
import sys

import requests

URL = "https://jsonplaceholder.typicode.com"

def are_arguments_valid(argv):
    valid_subprograms = ["read_user_posts", "read_post_comments", "read_user_posts_comments"]
    if len(argv) != 3 or argv[1] not in valid_subprograms:
        return False
    try:
        int(argv[2])
    except ValueError:
        return False
    return True

def read_user_posts(userid):
    params = {'userId': userid}
    response = requests.get(f"{URL}/posts", params=params)
    if response.status_code == 404:
        print("No results found!")
        return
    post_seq = json.loads(response.content)
    if not post_seq:
        print("No results found!")
        return
    print(f"Posts of user {userid}:")
    print()
    postlen = len(post_seq)
    for i, post in enumerate(post_seq):
        print(f"Post {i+1}/{postlen}:")
        print("ID:", post['id'])
        print("Title:", post['title'])
        print("Body:", post['body'])
        print()


def read_post_comments(postid):
    response = requests.get(f"{URL}/posts/{postid}/comments")
    if response.status_code == 404:
        print("No results found!")
        return
    seq = json.loads(response.content)
    if not seq:
        print("No results found!")
        return
    print(f"Comments of post {postid}:")
    print()
    for i, item in enumerate(seq):
        print(f"Comment {i+1}/{len(seq)}:")
        print("Name:", item["name"])
        print("Email:", item["email"])
        print("Body:", item["body"])
        print()



def read_user_posts_comments(userid):
    params = {'userId': userid}
    response = requests.get(f"{URL}/posts", params=params)
    if response.status_code == 404:
        print("No results found!")
        return
    post_seq = json.loads(response.content)
    if not post_seq:
        print("No results found!")
        return
    print(f"Posts of user {userid}:")
    print()
    postlen = len(post_seq)
    for i, post in enumerate(post_seq):
        print(f"Post {i+1}/{postlen}:")
        print("ID:", post['id'])
        print("Title:", post['title'])
        print("Body:", post['body'])

        response = requests.get(f"{URL}/posts/{post['id']}/comments")
        seq = json.loads(response.content)
        for i, item in enumerate(seq):
            print(" "*6+f"Comment {i + 1}/{len(seq)}:")
            print(" "*6+"Name:", item["name"])
            print(" "*6+"Email:", item["email"])
            body = item["body"]
            bodysplit = body.split("\n")
            indentbody = [bodysplit[0]] + [" "*6 + line for line in bodysplit[1:]]
            print(" "*6+"Body:", '\n'.join(indentbody))
            print()
        print()

def main():
    if not are_arguments_valid(sys.argv):
        print("Arguments Error!")
        sys.exit(1)
    chosen_subprogram = sys.argv[1]
    id_ = int(sys.argv[2])
    subprogram_map = {
        "read_user_posts": read_user_posts,
        "read_post_comments": read_post_comments,
        "read_user_posts_comments": read_user_posts_comments,
    }
    subprogram_map[chosen_subprogram](id_)



if __name__ == "__main__":
    main()