import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import matplotlib.pyplot as pyplot  # saving and plotting data:
import pickle
from matplotlib import style
from sklearn.metrics import r2_score


data = pd.read_csv("student_mat.csv", sep=";")

''' print(data.head())
    head() => It will return the first 5 rows of the dataset.
'''

# We are selecting only the required columns/attributes from the dataset.
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]
# print(data.head()) => will print the first 5 rows of following columns

# Label(s): Attribute(s) that we want to predict ie, we're using attributes to predict the label.
predict = "G3"
# Here, we want to predict the final grade of the student i.e. G3.

# x will have all the attributes except the label (attributes to be predicted), here G3
x = np.array(data.drop(predict, axis=1))
# y will have all the labels (attributes to be predicted), here G3
y = np.array(data[predict])
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)  # splitting the data into training and testing data


'''
best = 0  # best accuracy score
for _ in range(30):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size= 0.1)
    linear = linear_model.LinearRegression()
    linear.fit(x_train, y_train)
    accuracy= linear.score(x_test, y_test)
    print(accuracy)

    if accuracy > best:                                 # saving the best model, ie with highest accuracy
        best = accuracy
        with open("studentmodel.pickle", "wb") as f:    # saving the model
         pickle.dump(linear, f)                         # pickle.dump() => It is used to save the trained model in the studentmodel.pickle file. 
                                                        #It takes two arguments, which are the trained model and the file object.
'''

# loading the saved model
pickle_in = open("studentmodel.pickle", "rb")
linear = pickle.load(pickle_in)


# y= mx + b; m= coefficient, b= intercept
# print("Coefficients: \n", linear.coef_)
# print("Intercept: \n", linear.intercept_)

# Comparing predictions with actual values
predictions = linear.predict(x_test)
for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])

r2 = r2_score(y_test, predictions)
print("R-squared:", r2)

accuracy = linear.score(x_test, y_test)
print("Accuracy:", accuracy)

# Plotting the data
p = "absences"
style.use("ggplot")
pyplot.scatter(data[p], data["G3"])
pyplot.xlabel(p)
pyplot.ylabel("Final Grade")
pyplot.show()
