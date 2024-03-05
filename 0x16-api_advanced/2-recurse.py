#!/usr/bin/python3
"""
    a recursive function that queries the Reddit API and returns a
    list containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit,
    the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    # Base URL for Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"

    headers = {
        "User-Agent": "ALX:subscribers_counter:v1.0 (by /u/SosMrRaziel)"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check for invalid subreddit
    if response.status_code != 200:
        return None

    # Load response data
    data = response.json()
    posts = data.get("data", {}).get("children", [])

    # Add titles to the hot_list
    for post in posts:
        hot_list.append(post.get("data", {}).get("title"))

    # Get the 'after' value for pagination
    after = data.get("data", {}).get("after")

    # Recursive call if 'after' is present, else return the hot_list
    return recurse(subreddit, hot_list, after) if after else hot_list
