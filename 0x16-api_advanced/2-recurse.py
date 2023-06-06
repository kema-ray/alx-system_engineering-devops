#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""
import requests
import sys


def add_title(hot_list, posts):
    """
    Adds item into a list
    """
    if len(posts) == 0:
        return
    hot_list.append(posts[0]['data']['title'])
    posts.pop(0)
    add_title(hot_list, posts)


def recurse(subreddit, hot_list=[], after=None):
    """ Queries to Reddit API """
    user_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': user_agent
    }

    params = {
        'after': after
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    result = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)

    if result.status_code != 200:
        return None

    dic = result.json()
    posts = dic['data']['children']
    add_title(hot_list, posts)
    after = dic['data']['after']
    if not after:
        return hot_list
    return recurse(subreddit, hot_list=hot_list, after=after)