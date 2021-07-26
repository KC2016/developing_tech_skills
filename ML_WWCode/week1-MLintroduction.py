
import pandas as pd
from sklearn.model_selection import train_test_split

#Note: the link to the raw file should be used below
playgolf = pd.read_csv("https://raw.githubusercontent.com/WomenWhoCode/WWCodeDataScience/master/Intro_to_MachineLearning/data/PlayGolf.csv")
# print(playgolf)

# checking if the dataset is clean
# print(playgolf.isna().sum()) # count nan values
# print(playgolf.describe())   # give the main properties
# df = df.dropna()  # remove rows with at least one blank cell

y = playgolf["play"] #target response
X = playgolf.drop(["play"], axis=1) #example data/ input features
# print(y.shape)
# print(X.shape)
# print(y)
# print(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
print("Train-Test split complete!")
print("- X_train = " + str(X_train.shape) + " | " + str(X_train.columns.tolist()))
print("- y_train = " + str(y_train.shape))
print("- X_test = " + str(X_test.shape) + " | " + str(X_test.columns.tolist()))
print("- y_test = " + str(y_test.shape))

# analyse the train data, we are not allowed to analise the tests
print(X_train)
print(y_train)

train = X_train.copy()
train["play"] = y_train
# print(train)

'''What should I do next?
Analyze the dataset to see which columns are useful for the machine learning model.
Apply feature engineering, repeat step 1 till you are satistified with data
Apply Machine learning model on train data
Test it against our test data and generate the accuracy of the model
If the accuracy is not desirable, change parameters/algorithm in step 2 and repeat till 
ideal accuracy is achieved.
Train your machine learning model on 100% of the data and use this for any incoming prediction requests.'''

# importing pyplot and image from matplotlib 
import matplotlib.pyplot as plt 
import matplotlib.image as img 
  
# reading png image file 
im = img.imread('./images/MLprocesses2.png') 
# show image 
plt.imshow(im)
plt.show()
