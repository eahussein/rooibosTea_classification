import numpy as np
from sklearn.model_selection import GridSearchCV, cross_val_score, KFold
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import *
from sklearn import metrics

def cv (m, p, xtrain, ytrain, xtest, ytest):
    inner_cv = StratifiedKFold(n_splits=3)
    clf = GridSearchCV(m, p, scoring='accuracy', n_jobs=-1, cv=inner_cv, refit=True, verbose=0)
    clf.fit( xtrain,  ytrain)
    pred = clf.predict(xtest)
#     print(accuracy_score(ytest, pred))
    
    return accuracy_score(ytest, pred), clf


def get_accuracy_ml (m, p, xTrain, yTrain, xTest, yTest):
    accTot, clfTot = cv(m, p, xTrain, yTrain, xTest, yTest)
    jackTrainArr = []
    jackTestArr = []
            
    for i in range(len(xTrain)):
        x_train = np.delete(np.array(xTrain), i, 0)
        y_train = np.delete(np.array(yTrain), i, 0)
        
        scoreTrain, clf1 = cv(m, p, x_train, y_train, xTest, yTest)
        
        jackTrainArr.append(scoreTrain)
            
    for t in range (len(xTest)):
        x_test = np.delete(np.array(xTest), t, 0)
        y_test = np.delete(np.array(yTest), t, 0)
            
        y_predict = clfTot.predict(x_test)
        
        jackTestArr.append(accuracy_score(y_test, y_predict))  
            
    return  accTot, jackTrainArr, jackTestArr