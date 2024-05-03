import matplotlib.pyplot as plt
import pickle

# Load the user data
with open('ppw.userdata.pickle', 'rb') as f:
    user_data = pickle.load(f)

# Iterate over each user's data
for user in user_data:
    weeks = list(user[1].keys())
    posts = list(user[1].values())
    
    # Create a new figure for each user
    plt.figure()
    plt.plot(weeks, posts)
    plt.ylabel('Posts per week')
    plt.xlabel('Weeks since joining')
    plt.title(f'User {user[0]}')
    plt.show()