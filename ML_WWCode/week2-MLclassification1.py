'''
In this notebook we will build a classification model using Naive Bayes classifier from 
python's scikit learn library

Table of contents
Data Loading
Data Exploration
Visualization
Preprocessing
Bernoulli Naive Bayes model and its variants
Gaussian Naive Bayes
Ensemble of Bernoulli and Gaussian model
Model comparision using ROC curve
Loading Data

In this section we will import all the necessary packages and load the datasets we plan to work on. 
We will use the Hotel booking data and build a model to determine which customers will cancel 
their hotel booking

Dataset's source: https://www.kaggle.com/jessemostipak/hotel-booking-demand
'''

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as pyplot
from pylab import *
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import recall_score, precision_score, accuracy_score, f1_score
from sklearn.metrics import confusion_matrix, auc, roc_auc_score, roc_curve
import warnings
warnings.filterwarnings('ignore')

# load the data
file_path = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotels.csv'
df = pd.read_csv(file_path)

# Explore the dataset
# Understanding the data, its features and distribution 

# print(df.head())
# print(df.shape)
# print(df.dtypes # check the datatype of features
# print(df.columns) # feature list

# check for null values
percent_missing = df.isnull().sum() * 100 / len(df)
missing_value_df = pd.DataFrame({'column_name': df.columns, 'percent_missing': percent_missing})
missing_value_df.sort_values('percent_missing', ascending=False, inplace=True)
# print(missing_value_df)

'''Company, agent, country and children have null values. 
There are multiple techniques for imputing null value but for simplicity 
we impute them with 0. As company has a very high null value percentage 
we will drop the column.'''

# Let us create a copy of dataframe for backup and impute null with 0
backup_df = df.copy
df = df.drop('company', axis=1)
df = df.fillna(0)

# check that the df has no Null values
# print((df['agent'].isnull().sum()/len(df)) * 100)

''' 
Data Visualization
In this task, our target variable is is_cancelled 
which indicates if the booking was cancelled.
 1 --> canceled, 0 --> Not canceled'''

# df['is_canceled'].value_counts().plot(kind='pie', autopct='%1.1f%%')
# plt.show() 

# print('37% customers have cancelled their bookings. we see that our data in imbalanced')
# print(df.columns)

# Hotel feature count and distribution across 0 and 1 class
# df['hotel'].value_counts().plot(kind='pie', autopct = '%1.1f%%')
# plt.show() 

# sns.countplot(x='is_canceled', hue='hotel', data = df)
# plt.show() 

# print('''As data has higher city hotel reservation data points 
#          compared to resort, above observation is on par with 
#          same trend''')

# market segments
# df.groupby(['market_segment'])['is_canceled'].count().plot(kind='bar')
# plt.show() 

'''Feature Engineering
1- Derive new features using existing features
2- Remove irrelevant features
3- Transform existing features
4- Encoding categorical variables'''


# Split data into train test set in train:test=70:30 size
train, test = train_test_split(df, test_size=0.3, random_state = 42)
print(train.shape)
print(test.shape)

#Let us add weekend stay and weekday stay days to get total days of stay
train['total_days'] = train['stays_in_week_nights'] + train['stays_in_weekend_nights']
test['total_days'] = test['stays_in_week_nights'] + test['stays_in_weekend_nights']

# drop the weekend stay and weekday stay days features
train = train.drop('stays_in_week_nights', axis = 1).drop('stays_in_week_nights', axis = 1)