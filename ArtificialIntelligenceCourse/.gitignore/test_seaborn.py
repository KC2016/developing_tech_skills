import seaborn as sns
import pandas as pd

# # download the dataset
# import urllib.request

# relativPath = 'data'
# filename_LinearRegr = 'linear_regression_df.csv'
# url_LinearRegr = 'https://raw.githubusercontent.com/conordewey3/Hitchhikers-Guide-Machine-Learning/master/'+ filename_LinearRegr
# urllib.request.urlretrieve(url_LinearRegr, relativPath+'/'+filename_LinearRegr)

# from sklearn import linear_model
# df_LinearRegr = pd.read_csv(relativPath+'/'+filename_LinearRegr)

# df_LinearRegr = pd.read_csv(relativPath+'/'+'linear_regression_df.csv')
# print(df_LinearRegr)
# df_LinearRegr.columns = ['X', 'Y']
# print(df_LinearRegr.head())

# data = sns.load_dataset('df_LinearRegr')
# data.head(5)
import os
# url = 'https://raw.githubusercontent.com/conordewey3/Hitchhikers-Guide-Machine-Learning/master/linear_regression_df.csv'
# urllib.request.urlretrieve(url, 'data/linear_regression_df.csv')
df_LinearRegr = pd.read_csv('data/linear_regression_df.csv')
df_LinearRegr.columns = ['X', 'Y']
# print(df_LinearRegr)
# data = sns.load_dataset('df_LinearRegr')
data = sns.load_dataset('df_LinearRegr')
# print(data)