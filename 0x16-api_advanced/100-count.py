#!/usr/bin/python3
""" a recursive function that queries the Reddit API,
parses the title of all hot articles, and prints a sorted count
of given keywords (case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not). """

import requests


def count_words(subreddit, word_list, after='', word_count={}):
    # Base case: if 'after' is None, we've reached the last page
    if after is None:
        sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            if count > 0:
                print(f"{word}: {count}")
        return

    # Update the word_count dictionary with the current word_list counts
    if after == '':
        for word in word_list:
            word_count[word.lower()] = 0
    reddit = "https://www.reddit.com"
    # Prepare the request to the Reddit API
    url = f"{reddit}/r/{subreddit}/hot.json?limit=100&after={after}"
    headers = {
        "User-Agent": "ALX:subscribers_counter:v1.0 (by /u/SosMrRaziel)"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check for invalid subreddit
    if response.status_code != 200:
        return

    # Load the response data
    data = response.json()
    articles = data['data']['children']

    # Parse the titles and update word counts
    for article in articles:
        title = article['data']['title'].lower()
        for word in word_list:
            word_count[word.lower()] += title.split().count(word.lower())

    # Recursive call with the next page ('after')
    count_words(subreddit, word_list, data['data']['after'], word_count)
