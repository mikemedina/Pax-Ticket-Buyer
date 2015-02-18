import praw
from time import sleep


# user agent
user_agent = "PAX Ticket Buyer v1.0 by /u/80blite"
r = praw.Reddit(user_agent=user_agent)
r.login()

timer = 0
messages = 0

while True:

    submissions = []
    new_message = False

    # load history
    with open("history.txt", 'r') as f:
        history = f.read()

        # get 50 submissions
        top_50 = r.get_subreddit('paxpassexchange').get_new(limit=50)

        # create list of submissions not already in history
        submissions = [submission for submission in top_50\
        if "wts" in submission.title.lower() and submission.id not in history]

    # send message to seller and add submission title and id to history
    with open("history.txt", 'a') as f:
        for submission in submissions:
            msg = "Example message here"
            r.send_message(submission.author, 'Interested in your tickets!', msg)
            messages += 1
            new_message = True
            f.write(submission.title + ': ' + submission.id + '\n')

    sleep(60)
    timer += 60
    if new_message:
        print('Running time: ' + str(timer//60) + ' minutes')
        print("Submissions: " + str(len(submissions)))
        print('Messages sent: ' + str(messages))
        new_message = False
    if timer % 900 == 0:
        print('Running for {} minutes'.format(timer // 60))
