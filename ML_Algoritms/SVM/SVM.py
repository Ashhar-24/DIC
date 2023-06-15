import sklearn
from sklearn import datasets
from sklearn import svm

cancer = datasets.load_breast_cancer()  # loading the dataset from sklearn library 

print("Features: ", cancer.feature_names)
print("Labels: ", cancer.target_names)

x = cancer.data  # features
y = cancer.target  # labels

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.2)  # splitting the data into training and testing data

print(x_train, y_train)
classes = ['malignant' , 'benign']


