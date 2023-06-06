#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API
    """
    user_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': user_agent
    }

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    result = requests.get(url, headers=headers, allow_redirects=False)
    if result.status_code != 200:
        return 0
    dict = result.json()
    if 'data' not in dict:
        return 0
    if 'subscribers' not in dict.get('data'):
        return 0
    return result.json()['data']['subscribers']
