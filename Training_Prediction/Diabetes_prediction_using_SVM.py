# *********** Loading data from MongoDB ***********
import pymongo

# Connect to the MongoDB database
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Choose the collection
db = client["ADBS_Dataset"]
collection = db["diabetes"]

# Define the projection to exclude the "_id" field
projection = {"_id": 0}

# Execute a query with the projection
cursor = collection.find({}, projection)

# Create an empty list to store the results
data = []

# Iterate over the cursor and append each document to the list
for document in cursor:
    data.append(document)

# Print the results
# print(data[0])





# *********** Processing Data ***********
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

# Extract the features and labels from the data
X = []
Y = []

for feature in data:
    X.append([feature['Pregnancies'], feature['Glucose'], feature['BloodPressure'], feature['SkinThickness'], feature['Insulin'], feature['BMI'], feature['DiabetesPedigreeFunction'], feature['Age']])
    Y.append(feature['Outcome'])

# print(X[0])
# print(Y[0])

X = np.array(X)

# Split the data into training and test sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)





# *********** Training Model ***********
import pickle
from sklearn.svm import SVC

svm_model = SVC(kernel='linear', C=1, gamma='scale')
svm_model.fit(X_train, y_train)

pickle.dump(svm_model, open("../SavedModel/Diabetes_classifier", 'wb'))





# *********** Testing Model Accuracy ***********
# Evaluate the performance of the model on test data
from sklearn.metrics import accuracy_score

y_pred = svm_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy}")