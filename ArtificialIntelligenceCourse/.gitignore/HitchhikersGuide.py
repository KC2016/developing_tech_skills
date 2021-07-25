# The Hitchhiker's Guide to Machine Learning in Python

# Linear Regression
import pandas as pd
from sklearn import tree

# download the dataset
import urllib.request
relativPath = 'data'
filename_iris = 'iris_df.csv'
filename_LinearRegr = 'linear_regression_df.csv'
# filename_LogRegr = 'logistic_regression_df.csv'

url_iris = 'https://raw.githubusercontent.com/conordewey3/Hitchhikers-Guide-Machine-Learning/master/' + filename_iris
url_LinearRegr = 'https://raw.githubusercontent.com/conordewey3/Hitchhikers-Guide-Machine-Learning/master/'+ filename_LinearRegr
# url_LogRegr = 'https://raw.githubusercontent.com/conordewey3/Hitchhikers-Guide-Machine-Learning/master/' + filename_LogRegr
urllib.request.urlretrieve(url_iris, relativPath+'/'+filename_iris)
urllib.request.urlretrieve(url_LinearRegr, relativPath+'/'+filename_LinearRegr)
# urllib.request.urlretrieve(url_LogRegr, relativPath+'/'+filename_LogRegr)

# df_iris = pd.read_csv(relativPath+'/'+filename_iris)
# df_iris.columns = ['X1', 'X2', 'X3', 'X4', 'Y']
# # print(df_iris.head())

# from sklearn import linear_model
df_LinearRegr = pd.read_csv(relativPath+'/'+filename_LinearRegr, delimiter=';')
df_LinearRegr.columns = ['X', 'Y']
print(df_LinearRegr.head())

# Visualization
import seaborn as sns
import matplotlib as plt

# data = sns.load_dataset('df_LinearRegr')
# data.head(5)

# sns.set_context('notebook', font_scale=1.1)
# sns.set_style('ticks')
# sns.lmplot('X','Y', data )
# plt.ylabel('Response')  #erro aqui
# plt.xlabel('Explanatory')
# plt.show()