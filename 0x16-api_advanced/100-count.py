import praw

def count_words(subreddit, word_list, limit=10, count_dict=None, after=None):
    # Create a new Reddit instance
    reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                         client_secret='YOUR_CLIENT_SECRET',
                         user_agent='YOUR_USER_AGENT')

    # Initialize the count dictionary if it doesn't exist
    if count_dict is None:
        count_dict = {}

    # Get the hot articles from the subreddit
    hot_articles = reddit.subreddit(subreddit).hot(limit=limit, params={"after": after})

    # Loop through each article and count the occurrences of each word in the title
    for article in hot_articles:
        title = article.title.lower()
        for word in word_list:
            if word.lower() in title and 'java' not in title:
                count_dict[word] = count_dict.get(word, 0) + 1

    # If there are more articles, recursively call the function with the after parameter set
    if hot_articles.after is not None:
        count_words(subreddit, word_list, limit=limit, count_dict=count_dict, after=hot_articles.after)

    # Once all articles have been processed, print the sorted count dictionary
    sorted_count = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_count:
        print(f"{word}: {count}")
