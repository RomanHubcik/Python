# -*- coding: utf-8 -*-

#import the libraries
import numpy as np
import pandas as pd
# Import the linear and logistic regression class
from sklearn.linear_model import LinearRegression, LogisticRegression
# Sklearn also has a helper that makes it easy to do cross-validation
from sklearn.model_selection import KFold, cross_val_score


#import the dataset, train data
titanic = pd.read_csv('titanic_train.csv')
print(titanic.describe())
#titanic['Age']


#find unique values
print(titanic["Sex"].unique())
print(titanic["Embarked"].unique())

#fill missing data
titanic['Age'] = titanic['Age'].fillna(titanic['Age'].median())
titanic["Fare"] = titanic["Fare"].fillna(titanic["Fare"].median())
titanic['Embarked'] = titanic['Embarked'].fillna('S')

#convert to numeric values
titanic.loc[titanic['Sex'] == 'male', 'Sex'] = 0
titanic.loc[titanic['Sex'] == 'female', 'Sex'] = 1
titanic.loc[titanic['Embarked'] == 'S', 'Embarked'] = 0
titanic.loc[titanic['Embarked'] == 'C', 'Embarked'] = 1
titanic.loc[titanic['Embarked'] == 'Q', 'Embarked'] = 2

#first prediction
#cross-validation as a firewall against model overfitting
# The columns we'll use to predict the target
predictors = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]

# Initialize our algorithm class
alg = LinearRegression()
# Generate cross-validation folds for the titanic data set
# It returns the row indices corresponding to train and test
# We set random_state to ensure we get the same splits every time we run this
kf = KFold(3, random_state=1)

predictions = []
for train, test in kf.split(titanic):
        # The predictors we're using to train the algorithm  
    # Note how we only take the rows in the train folds
    train_predictors = (titanic[predictors].iloc[train,:])
    # The target we're using to train the algorithm
    train_target = titanic["Survived"].iloc[train]
    # Training the algorithm using the predictors and target
    alg.fit(train_predictors, train_target)
    # We can now make predictions on the test fold
    test_predictions = alg.predict(titanic[predictors].iloc[test,:])
    predictions.append(test_predictions)
    
#evaluate the error
# The predictions are in three separate NumPy arrays  
# Concatenate them into a single array, along the axis 0 (the only 1 axis) 
predictions = np.concatenate(predictions, axis=0)

# Map predictions to outcomes (the only possible outcomes are 1 and 0)
predictions[predictions > .5] = 1
predictions[predictions <=.5] = 0
accuracy = len(predictions[predictions == titanic['Survived']]) / len(predictions)

# Initialize the algorithm class
alg = LogisticRegression(random_state=1)

# Compute the accuracy score for all the cross-validation folds; this is much simpler than what we did before
scores = cross_val_score(alg, titanic[predictors], titanic["Survived"], cv=3)
# Take the mean of the scores (because we have one for each fold)
print(scores.mean())






#test data
titanic_test = pd.read_csv("titanic_test.csv")
titanic_test["Age"] = titanic_test["Age"].fillna(titanic["Age"].median())
titanic_test["Fare"] = titanic_test["Fare"].fillna(titanic_test["Fare"].median())
titanic_test.loc[titanic_test["Sex"] == "male", "Sex"] = 0 
titanic_test.loc[titanic_test["Sex"] == "female", "Sex"] = 1
titanic_test["Embarked"] = titanic_test["Embarked"].fillna("S")

titanic_test.loc[titanic_test["Embarked"] == "S", "Embarked"] = 0
titanic_test.loc[titanic_test["Embarked"] == "C", "Embarked"] = 1
titanic_test.loc[titanic_test["Embarked"] == "Q", "Embarked"] = 2

# Initialize the algorithm class
alg = LogisticRegression(random_state=1)

# Train the algorithm using all the training data
alg.fit(titanic[predictors], titanic["Survived"])

# Make predictions using the test set
predictions = alg.predict(titanic_test[predictors])


# Create a new dataframe with only the columns Kaggle wants from the data set
submission = pd.DataFrame({
        "PassengerId": titanic_test["PassengerId"],
        "Survived": predictions
    })
submission.to_csv("kaggle_simple.csv", index=False)