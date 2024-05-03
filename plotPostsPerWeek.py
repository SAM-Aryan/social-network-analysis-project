import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn import linear_model, pipeline, preprocessing
import numpy as np
import pickle

# Load the data
with open('ppw.weeks.pickle', 'rb') as f:
    weeks = pickle.load(f)
with open('ppw.posts_per_week.pickle', 'rb') as f:
    posts_per_week = pickle.load(f)
'''with open('ppw.avg.pickle', 'rb') as f:
    avg = pickle.load(f)'''
with open('ppw.avg_weeks.pickle', 'rb') as f:
    avg_weeks = pickle.load(f)

# Convert data to NumPy arrays
weeks_array = np.asarray(weeks)
ppw_array = np.asarray(posts_per_week)

# Create the pipeline
polynomial_features = preprocessing.PolynomialFeatures(degree=2, include_bias=False)
linear_regression = linear_model.LassoLars()
pipeline = pipeline.Pipeline([("polynomial_features", polynomial_features),
                               ("linear_regression", linear_regression)])

# Fit the pipeline
pipeline.fit(weeks_array[:, np.newaxis], ppw_array)

# Create a separate linear regression model
clf = linear_model.LassoLars()
clf.fit(weeks_array[:, np.newaxis], ppw_array)

# Plot the data
plt.figure(figsize=(10, 6))  # Set a larger figure size
plt.scatter(weeks, posts_per_week, label='Data')
plt.plot(weeks_array, pipeline.predict(weeks_array[:, np.newaxis]), color='red', label='Polynomial Regression')
#plt.scatter(avg_weeks, avg, color='green', label='Average')
# plt.scatter(weeks, clf.predict(weeks_array[:, np.newaxis]), color='green')  # Uncomment if needed
plt.ylabel('Posts per week')
plt.xlabel('Weeks since joining')
plt.legend()  # Add a legend
plt.show()