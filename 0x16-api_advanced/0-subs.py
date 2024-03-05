#!/usr/bin/python3
" subscribers counter"
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit"""
    # Set the custom user-agent
    headers = {
        'User-Agent': 'ALX:subscribers_counter:v1.0 (by /u/SosMrRaziel)'}
    # Make a GET request to the subreddit's about.json endpoint
    response = requests.get(
        'https://www.reddit.com/r/{}/about.json'.format(
            subreddit), headers=headers)
    # Check the status code and the json data
    if response.status_code == 200 and response.json().get('kind') == 't5':
        # Return the subscriber count
        return response.json().get('data').get('subscribers')
    else:
        # Return 0 for invalid subreddit
        return 0
