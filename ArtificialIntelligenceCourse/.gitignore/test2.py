import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree # NEW, was missing
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.externals.six import StringIO
import pydotplus as pydot
import matplotlib.image as mpimg
from sklearn.metrics import classification_report, confusion_matrix
from IPython.display import Image 
from sklearn.metrics import accuracy_score # NEW, was missing
import itertools # NEW, was missing

# download the dataset
import urllib.request
    
filename = 'dataset_einstein.csv'
relativPath = '03-DecisionTree/data'

url = 'https://raw.githubusercontent.com/diogocortiz/Crash-Course-IA/master/ArvoreDecis%C3%A3o/' + filename
urllib.request.urlretrieve(url, relativPath+'/'+filename)

# import the dataset to a dataframe
df = pd.read_csv(relativPath+'/'+'dataset_einstein.csv', delimiter=';')
print(type(df))