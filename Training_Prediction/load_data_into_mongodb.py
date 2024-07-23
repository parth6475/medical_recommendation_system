#CSV to JSON Conversion
import csv
from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017/") 
db = client['ADBS_Dataset']
collection = db['diabetes']

# this is for heart disease
# header= ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal", "target"]
# header= ["\ufeffage".strip(), "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal", "target"]
# csvfile = open('/home/bhagirath/Downloads/ADBS/Assignment2/Data/heart_disease_data.csv', 'r')

# this is for diabetes
header= [ "Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age", "Outcome"]
csvfile = open('/home/bhagirath/Downloads/ADBS/Assignment2/Data/diabetes.csv', 'r')


reader = csv.DictReader( csvfile )

for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    collection.insert_one(row)


# print(header)
# print(next(reader))