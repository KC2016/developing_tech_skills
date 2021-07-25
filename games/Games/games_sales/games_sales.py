import pandas as pd

games_sales_df = pd.read_csv('Games/games_sales/vgsales.csv')
# print(games_sales_df)
# print(games_sales_df.shape)
# print(type(games_sales_df))
# print(games_sales_df.describe)
# print(games_sales_df.info())
# print(games_sales_df.mode())
# print(games_sales_df.mean())
# print(games_sales_df.head())
# print(games_sales_df.tail())
# print(games_sales_df.columns)
# print(games_sales_df.columns[games_sales_df.isnull().any()].tolist()) #Find columns with Nans in them
# print(games_sales_df.isnull().sum())

# #Get counts of Nan values
# print("Missing Value Count - " + str(len(games_sales_df)) + " rows")
# print("Year: " + str(games_sales_df['Year'].isna().sum()))
# print("Publisher " + str(games_sales_df['Publisher'].isna().sum()))

# data_frame = df.dropna() # remove all rows with nan values

#Drop NA's - lets drop rows where has null (Publisher)
print("Before dropping - " + str(len(games_sales_df)) + " rows")
games_sales_df = games_sales_df[~games_sales_df['Publisher'].isna()] 
games_sales_df = games_sales_df[~games_sales_df['Year'].isna()]
print("After dropping - " + str(len(games_sales_df)) + " rows")

# percent_nan_in_publishers = 58/16598
# percent_nan_in_years = 271/16598
# print(percent_nan_in_publishers)
# print(percent_nan_in_years)

'''when we have many nan values and want to fill them
Fill NA's - Since Cabin is mostly empty, lets fill it with the most frequent value
most_frequent_cabin = df['Cabin'].value_counts().idxmax()
print("Most Frequent Cabin = " + most_frequent_cabin)
print("NA count before fill = " + str(len(df[df['Cabin'].isna()])))
df['Cabin'] = df['Cabin'].fillna(most_frequent_cabin)
print("NA count after fill = " + str(len(df[df['Cabin'].isna()]))) '''