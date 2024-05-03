import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn import linear_model, pipeline, preprocessing
import numpy as np
import pickle

# Load the user data
with open('ppw.userdata.pickle', 'rb') as f:
    user_data = pickle.load(f)

i = 0
for user in user_data:
    weeks = sorted(user[1].keys())
    skip = False
    prev_week = 0
    for week in weeks:
        if week - prev_week >= 52:
            skip = False
            break
        prev_week = week
    if skip:
        continue

    posts = [value for key, value in sorted(user[1].items())]
    skip = False
    # remove outlier(s):
    for post in posts:
        if post > 1600:
            print('skipping')
            skip = True
            break
    if skip:
        continue

    plt.figure()  # Create a new figure for each user
    plt.plot(weeks, posts)
    i += 1
    print(i)
    plt.ylabel('Posts per week')
    plt.xlabel('Weeks since joining')
    plt.title(f'User {user[0]}')  # Assuming user[0] contains the user's ID or name
    plt.show()