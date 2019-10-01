from  sklearn import  datasets
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score


def test(x,y,percent, name):
    x_t,x_ts,y_t,y_ts = train_test_split(x,y,test_size=(percent/100)) 
    classifier = tree.DecisionTreeClassifier()
    classifier.fit(x_t,y_t)
    predictions=classifier.predict(x_ts)
    print("The accuracy {} percent training of the {} database is {} percent".format(percent, name, round(accuracy_score(y_ts,predictions) * 100)))

# iris = datasets.load_iris()
# wine = datasets.load_wine()
# breastC = datasets.load_breast_cancer()
# diabetes = datasets.load_diabetes()


#Iris
currentDB = datasets.load_iris()
print(currentDB.data.shape)

x=currentDB.data
y=currentDB.target
per = 50
while per > 0:
    test(x,y,per,"iris") 
    per = per - 10

#Wine
currentDB = datasets.load_wine()
print(currentDB.data.shape)

x=currentDB.data
y=currentDB.target
per = 50
while per > 0:
    test(x,y,per,"wine") 
    per = per - 10

#Breast Cancer
currentDB = datasets.load_breast_cancer()
print(currentDB.data.shape)

x=currentDB.data
y=currentDB.target
per = 50
while per > 0:
    test(x,y,per,"breast cancer") 
    per = per - 10

#Diabetes
currentDB = datasets.load_diabetes()
print(currentDB.data.shape)

x=currentDB.data
y=currentDB.target
per = 50
while per > 0:
    test(x,y,per,"diabetes")
    per = per - 10
