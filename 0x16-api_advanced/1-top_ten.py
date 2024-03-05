#!/usr/bin/python3
"""
    a function that queries the Reddit API and prints
    the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """ print data and title """
    base_url = "https://www.reddit.com/"
    headers = {
        "User-Agent": "ALX:subscribers_counter:v1.0 (by /u/SosMrRaziel)"}

    # Construct the full URL for the subreddit's hot listing
    url = base_url + "r/" + subreddit + "/hot.json"

    # Send a GET request to the API and get the response
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response status code is 200 (OK) and the subreddit exists
    if response.status_code == 200:
        # Get the first 10 posts from the response data
        posts = response.json()["data"]["children"][:10]
        # Print the titles of the posts
        for post in posts:
            print(post["data"]["title"])
    else:
        # Print None if the subreddit is invalid or empty
        print(None)
