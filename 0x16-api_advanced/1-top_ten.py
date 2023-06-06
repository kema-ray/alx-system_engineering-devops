#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API
    """
    user_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': user_agent
    }

    params = {
        'limit': 10
    }
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    results = requests.get(url,headers=headers,
                           parameters=params,
                           allow_redirects=False)

    if results.status_code != 200:
        print(None)
        return
    dict= results.json()
    posts = dict['data']['children']
    if len(posts) is 0:
        print(None)
    else:
        for post in posts:
            print(post['data']['title'])
