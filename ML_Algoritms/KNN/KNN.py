import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing

data = pd.read_csv("car.data")
# print(data.head()) # printing first 5 rows of the data

# As we can see that the data/attributes is not numerical so we need to convert it into numerical data
# converting non-numerical data to numerical data using preprocessing library of sklearn (numpy array)
le = preprocessing.LabelEncoder()
# converting buying column to numerical data
buying = le.fit_transform(list(data["buying"]))
# converting maint column to numerical data
maint = le.fit_transform(list(data["maint"]))
# converting door column to numerical data
door = le.fit_transform(list(data["door"]))
# converting persons column to numerical data
persons = le.fit_transform(list(data["persons"]))
# converting lug_boot column to numerical data
lug_boot = le.fit_transform(list(data["lug_boot"]))
# converting safety column to numerical data
safety = le.fit_transform(list(data["safety"]))
# converting class column to numerical data
cls = le.fit_transform(list(data["class"]))

predict = "class"  # this is the column which we want to predict

# Now we will combine all the attributes into a single list
x = list(zip(buying, maint, door, persons, lug_boot, safety)) # x is the features of the data (attributes) 
y = list(cls) # y is the label of the data (class) 

# Now we will split the data into training and testing data
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1) # test_size=0.1 means 10% of the data will be used for testing

model = KNeighborsClassifier(n_neighbors=9)  # n_neighbors is the value of k
model.fit(x_train, y_train)
acc = model.score(x_test, y_test)
print(acc)

predicted = model.predict(x_test)
names = ["unacc", "acc", "good", "vgood"]   # [0, 1, 2, 3] are the numerical values of the class names 

# printing the predicted values and the actual values of the test data
for x in range(len(predicted)):
    print("Predicted:", names[predicted[x]], " Data:", x_test[x], " Actual:", names[y_test[x]])
    # Now we will print the neighbors of each point in our testing data and see how many of them are in the same class 
    # n = model.kneighbors([x_test[x]], 9, True)
    # print("N:", n) # n is a tuple of 2 arrays, 1st array is the distance and 2nd array is the index of the neighbors
    