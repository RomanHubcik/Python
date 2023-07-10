import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import seaborn as sns
import operator
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import KFold
from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.feature_selection import SelectKBest, f_classif


#-----------------------start of the train data--------------------------------
titanic = pd.read_csv('titanic_train.csv')
#find unique charcters
print(titanic["Sex"].unique())
print(titanic["Embarked"].unique())
#end
titanic['Age'] = titanic['Age'].fillna(titanic['Age'].median())
titanic['Embarked'] = titanic['Embarked'].fillna('S')
titanic.loc[titanic['Sex'] == 'male', 'Sex'] = 0
titanic.loc[titanic['Sex'] == 'female', 'Sex'] = 1
titanic.loc[titanic['Embarked'] == 'S', 'Embarked'] = 0
titanic.loc[titanic['Embarked'] == 'C', 'Embarked'] = 1
titanic.loc[titanic['Embarked'] == 'Q', 'Embarked'] = 2
#new features
titanic["FamilySize"] = titanic["SibSp"] + titanic["Parch"]
titanic["NameLength"] = titanic["Name"].apply(lambda x: len(x))
#end
#extract passengers Name and Title from name
def get_title(name):
    title_search = re.search(' ([A-Za-z]+)\.', name)
    if title_search:
        return title_search.group(1)
    return ""
titles = titanic["Name"].apply(get_title)
print(pd.value_counts(titles))
title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Dr": 5, "Rev": 6, "Major": 7, "Col": 7, "Mlle": 8, "Mme": 8, "Don": 9, "Lady": 10, "Countess": 10, "Jonkheer": 10, "Sir": 9, "Capt": 7, "Ms": 2}
for k,v in title_mapping.items():
    titles[titles == k] = v
print(pd.value_counts(titles))
titanic["Title"] = titles
#end
#feature that indicates which family passengers belong to
family_id_mapping = {}
def get_family_id(row):
    last_name = row["Name"].split(",")[0]
    family_id = "{0}{1}".format(last_name, row["FamilySize"])
    if family_id not in family_id_mapping:
        if len(family_id_mapping) == 0:
            current_id = 1
        else:
            current_id = (max(family_id_mapping.items(), key=operator.itemgetter(1))[1] + 1)
        family_id_mapping[family_id] = current_id
    return family_id_mapping[family_id]
family_ids = titanic.apply(get_family_id, axis=1)
family_ids[titanic["FamilySize"] < 3] = -1
print(pd.value_counts(family_ids))
titanic["FamilyId"] = family_ids
#end
#find which features are the best with univariate feature selection
predictors = ["Pclass", "Sex", "Age", "SibSp", "Embarked", 
              "Parch", "Fare", "FamilySize", "Title", "FamilyId", "NameLength"]
selector = SelectKBest(f_classif, k=5)
selector.fit(titanic[predictors], titanic["Survived"])
scores = -np.log10(selector.pvalues_)
plt.bar(range(len(predictors)), scores)
plt.xticks(range(len(predictors)), predictors, rotation='vertical')
plt.show()
#see the plot and pick only the five best features ------------------do not use 
predictors = ["Pclass", "Sex", "Age", "SibSp", "Embarked", 
              "Parch", "Fare", "FamilySize", "Title", "FamilyId", "NameLength"]
alg = RandomForestClassifier(random_state=1, n_estimators=50, min_samples_split=8, min_samples_leaf=4)
scores = cross_validation.cross_val_score(alg, titanic[predictors], titanic["Survived"], cv=3)
print(scores.mean()) #even if I use all of them, result is slightly worse than selection
#end-----------------------------------------------------------------do not use
predictors = ["Pclass", "Sex", "Age", "SibSp", "Embarked"]
alg = RandomForestClassifier(random_state=1, n_estimators=50, min_samples_split=5, min_samples_leaf=5)
kf = cross_validation.KFold(titanic.shape[0], n_folds=3, random_state=1)
scores = cross_validation.cross_val_score(alg, titanic[predictors], titanic["Survived"], cv=kf)
print(scores.mean())  
sns.distplot(scores)  
#----------------------------end of the train data-----------------------------






#training_test
titanic_test = pd.read_csv('titanic_test.csv')
titanic_test['Age'] = titanic_test['Age'].fillna(titanic_test['Age'].median())
titanic_test['Embarked'] = titanic_test['Embarked'].fillna('S')
titanic_test.loc[titanic_test['Sex'] == 'male', 'Sex'] = 0
titanic_test.loc[titanic_test['Sex'] == 'female', 'Sex'] = 1
titanic_test.loc[titanic_test['Embarked'] == 'S', 'Embarked'] = 0
titanic_test.loc[titanic_test['Embarked'] == 'C', 'Embarked'] = 1
titanic_test.loc[titanic_test['Embarked'] == 'Q', 'Embarked'] = 2
titanic_test["FamilySize"] = titanic_test["SibSp"] + titanic_test["Parch"]
titanic_test["NameLength"] = titanic_test["Name"].apply(lambda x: len(x))
def get_title(name):
    title_search = re.search(' ([A-Za-z]+)\.', name)
    if title_search:
        return title_search.group(1)
    return ""
titles = titanic_test["Name"].apply(get_title)
print(pd.value_counts(titles))
title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Dr": 5, "Rev": 6, "Major": 7, "Col": 7, "Mlle": 8, "Mme": 8, "Don": 9, "Lady": 10, "Countess": 10, "Jonkheer": 10, "Sir": 9, "Capt": 7, "Ms": 2}
for k,v in title_mapping.items():
    titles[titles == k] = v
print(pd.value_counts(titles))
titanic_test["Title"] = titles
family_id_mapping = {}
def get_family_id(row):
    last_name = row["Name"].split(",")[0]
    family_id = "{0}{1}".format(last_name, row["FamilySize"])
    if family_id not in family_id_mapping:
        if len(family_id_mapping) == 0:
            current_id = 1
        else:
            current_id = (max(family_id_mapping.items(), key=operator.itemgetter(1))[1] + 1)
        family_id_mapping[family_id] = current_id
    return family_id_mapping[family_id]
family_ids = titanic_test.apply(get_family_id, axis=1)
family_ids[titanic_test["FamilySize"] < 3] = -1
print(pd.value_counts(family_ids))
titanic_test["FamilyId"] = family_ids
predictors = ["Pclass", "Sex", "Age", "SibSp", "Embarked"]
alg = RandomForestClassifier(random_state=1, n_estimators=50, min_samples_split=5, min_samples_leaf=5)
kf = cross_validation.KFold(titanic.shape[0], n_folds=3, random_state=1)
scores = cross_validation.cross_val_score(alg, titanic[predictors], titanic["Survived"], cv=kf)
print(scores.mean())  
#end


predictors = ["Pclass", "Sex", "Age", "SibSp", "Embarked"]
#algorithms = [RandomForestClassifier(random_state=1, n_estimators=50, min_samples_split=5, min_samples_leaf=5)]
#algorithms = [
#    [GradientBoostingClassifier(random_state=1, n_estimators=25, max_depth=3), predictors],
#   [LogisticRegression(random_state=1), ["Pclass", "Sex", "Age", "SibSp", "Embarked"]],
#   [RandomForestClassifier(random_state=1, n_estimators=50, min_samples_split=5, min_samples_leaf=5)]]
algorithms = [
   [RandomForestClassifier(random_state=1, n_estimators=50, min_samples_split=5, min_samples_leaf=5),
    ["Pclass", "Sex", "Age", "SibSp", "Embarked"]]
   ]
full_predictions = []
for algr, predictors in algorithms:
    algr.fit(titanic[predictors], titanic["Survived"])
    predictions = algr.predict_proba(titanic_test[predictors].astype(float))[:,1]
    full_predictions.append(predictions)
#not used
predictions = predictions.astype(int)
full_predictions = np.concatenate(full_predictions, axis=0)
#predictions = (full_predictions[0] * 3 + full_predictions[1]) / 4
full_predictions[full_predictions <= .5] = 0
full_predictions[full_predictions > .5] = 1

#not used
submission = pd.DataFrame({
        "PassengerId": titanic_test["PassengerId"],
        "Survived": full_predictions
    })
submission.to_csv("kaggle_custom3.csv", index=False)











#----------------------------start of the test data----------------------------
titanic_test = pd.read_csv('titanic_test.csv')
titles = titanic_test["Name"].apply(get_title)
title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Dr": 5, "Rev": 6, "Major": 7, "Col": 7, "Mlle": 8, "Mme": 8, "Don": 9, "Lady": 10, "Countess": 10, "Jonkheer": 10, "Sir": 9, "Capt": 7, "Ms": 2, "Dona": 10}
for k,v in title_mapping.items():
    titles[titles == k] = v
titanic_test["Title"] = titles
titanic_test['Age'] = titanic_test['Age'].fillna(titanic_test['Age'].median())
titanic_test['Embarked'] = titanic_test['Embarked'].fillna('S')
titanic_test.loc[titanic_test['Sex'] == 'male', 'Sex'] = 0
titanic_test.loc[titanic_test['Sex'] == 'female', 'Sex'] = 1
titanic_test.loc[titanic_test['Embarked'] == 'S', 'Embarked'] = 0
titanic_test.loc[titanic_test['Embarked'] == 'C', 'Embarked'] = 1
titanic_test.loc[titanic_test['Embarked'] == 'Q', 'Embarked'] = 2
print(titanic_test["Sex"].unique())
print(titanic_test["Embarked"].unique())
print(pd.value_counts(titanic_test["Title"]))
titanic_test["FamilySize"] = titanic_test["SibSp"] + titanic_test["Parch"]
print(family_id_mapping)
family_ids = titanic_test.apply(get_family_id, axis=1)
family_ids[titanic_test["FamilySize"] < 3] = -1
titanic_test["FamilyId"] = family_ids
titanic_test["NameLength"] = titanic_test["Name"].apply(lambda x: len(x))
predictors = ["Pclass", "Sex", "Age", "SibSp", "Embarked", "Title", "FamilySize", "FamilyId"]
algorithms = [
    [GradientBoostingClassifier(random_state=1, n_estimators=25, max_depth=3), predictors],
    [LogisticRegression(random_state=1), ["Pclass", "Sex", "Age", "SibSp", "Embarked", "Title", "FamilySize", "FamilyId"]]
]
full_predictions = []
for alg, predictors in algorithms:
    alg.fit(titanic[predictors], titanic["Survived"])
    predictions = alg.predict_proba(titanic_test[predictors].astype(float))[:,1]
    full_predictions.append(predictions)
predictions = (full_predictions[0] * 3 + full_predictions[1]) / 4
predictions[predictions <= .5] = 0
predictions[predictions > .5] = 1
predictions = predictions.astype(int)
submission = pd.DataFrame({
        "PassengerId": titanic_test["PassengerId"],
        "Survived": predictions
    })
submission.to_csv("kaggle_custom3.csv", index=False)