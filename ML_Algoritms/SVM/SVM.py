import sklearn
from sklearn import datasets
from sklearn import svm
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier  # importing the KNN classifier from sklearn library for comparing with SVM

cancer = datasets.load_breast_cancer()  # loading the dataset from sklearn library 

# print("Features: ", cancer.feature_names)
# print("Labels: ", cancer.target_names)

x = cancer.data  # features
y = cancer.target  # labels

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.2)  # splitting the data into training and testing data

# print(x_train, y_train)
classes = ['malignant' , 'benign']

clf = svm.SVC(kernel= "linear" , C=2)  # creating the SVM classifier with soft-margin (C=2 is the soft-margin parameter | hard-margin C=0)
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)

accuracy = metrics.accuracy_score(y_test, y_pred)
print("SVM: ", accuracy)

# Comparing the SVM with KNN classifier
clfy = KNeighborsClassifier(n_neighbors=9)
clfy.fit(x_train, y_train)

y_pred = clfy.predict(x_test)

acc = metrics.accuracy_score(y_test, y_pred)
print("KNN: ", acc)