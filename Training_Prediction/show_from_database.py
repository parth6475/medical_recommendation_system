import pymongo
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def diabetes_prediction_from_database():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["ADBS_Dataset"]
    collection = db["diabetes"]
    projection = {"_id": 0}
    cursor = collection.find({}, projection)
    data = []
    for document in cursor:
        data.append(document)

    X = []
    Y = []
    for feature in data:
        X.append([feature['Pregnancies'], feature['Glucose'], feature['BloodPressure'], feature['SkinThickness'], feature['Insulin'], feature['BMI'], feature['DiabetesPedigreeFunction'], feature['Age']])
        Y.append(feature['Outcome'])

    X = np.array(X)
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)


    svm_model = SVC(kernel='linear', C=1, gamma='scale')
    svm_model.fit(X_train, y_train)

    y_pred = svm_model.predict(X_test)
    result= list(zip(y_test, y_pred))
    result= list(zip(X_test, result))
    
    return result






def heart_disease_prediction_from_database():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["ADBS_Dataset"]
    collection = db["heart_disease"]
    projection = {"_id": 0}
    cursor = collection.find({}, projection)
    data = []
    for document in cursor:
        data.append(document)
    
    X = []
    Y = []
    for feature in data:
        X.append([feature["\ufeffage".strip()], feature['sex'], feature['cp'], feature['trestbps'], feature['chol'], feature['fbs'], feature['restecg'], feature['thalach'], feature['exang'], feature['oldpeak'], feature['slope'], feature['ca'], feature['thal']])
        Y.append(feature['target'])
    X = np.array(X)
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)


    svm_model = SVC(kernel='linear', C=1, gamma='scale')
    svm_model.fit(X_train, y_train)

    y_pred = svm_model.predict(X_test)
    result= list(zip(y_test, y_pred))
    result= list(zip(X_test, result))
    
    return result