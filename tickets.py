import praw
from time import sleep


# user agent
user_agent = "PAX Ticket Buyer v1.0 by /u/80blite"
r = praw.Reddit(user_agent=user_agent)
r.login('80blite', 'ihatesh33p')

timer = 0
while True:

    submissions = []

    # load history
    with open("history.txt", 'r') as f:
        history = f.read()
                #if history:
                #    print('history: \n' + history)
                #else:
                #    print('No history')

        # assign subreddit
        top_50 = r.get_subreddit('paxpassexchange').get_new(limit=50)

        # list of submissions not already in history
        submissions = [submission for submission in top_50\
        if "wts" in submission.title.lower() and submission.id not in history]
        print("Submissions: " + str(len(submissions)))

    # send link to user and add submission.id to history
    with open("history.txt", 'a') as f:
        for submission in submissions:
            msg = "Hi there,\n\nI'm trying to take my wife to PAX as a Valentine's day gift. She thinks she didn't get anything and she's been wanting to go to PAX for a few years now.\n\nAnway, I'm really interested in your tickets and they would mean a lot to my wife and I. Message me back if you'd like to do business =)\n\nThanks so much,\n\n-Mike"
            r.send_message(submission.author, 'Interested in your tickets!', msg)
            print('Message sent')
            f.write(submission.title + ': ' + submission.id + '\n')

    print('Done!')
    sleep(900)
    timer += 900
    print('Running time: ' + str(timer/60))

