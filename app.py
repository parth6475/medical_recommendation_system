from flask import Flask, render_template, request
import pickle
from Training_Prediction.show_from_database import diabetes_prediction_from_database,heart_disease_prediction_from_database

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('index.html')





# ******* this is for home page button ******* 
@app.route("/diabetes", methods=['GET', 'POST'])
def diabetes():
    return render_template('diabetes.html')

@app.route("/heart_disease", methods=['GET', 'POST'])
def heart_disease():    
    return render_template('heart_disease.html')





# ******* this is for Diabetes ******* 
@app.route("/Test_Model_Diabetes", methods=['GET', 'POST'])
def Test_Model_Diabetes():
    result=diabetes_prediction_from_database()
    return render_template('show_from_database.html',Disease='Diabetes',result=result)

@app.route("/Predict_Diabetes", methods=['GET', 'POST'])
def Predict_Diabetes():    
    return render_template('predict_diabetes.html')





# ******* this is for Heart Disease ******* 
@app.route("/Test_Model_Heart_Disease", methods=['GET', 'POST'])
def Test_Model_Heart_Disease():
    result=heart_disease_prediction_from_database()
    return render_template('show_from_database.html',Disease='Heart Disease',result=result)

@app.route("/Predict_Heart_Disease", methods=['GET', 'POST'])
def Predict_Heart_Disease():    
    return render_template('predict_heart_disease.html')





# ******* this is for Diabetes_Prediction ******* 
@app.route('/Diabetes_Prediction', methods=['POST'])
def Diabetes_Prediction():
    # Get the form data from the request object
    pregnancies = float(request.form['pregnancies'])
    glucose = float(request.form['glucose'])
    bp = float(request.form['blood-pressure'])
    skin = float(request.form['skin-thickness'])
    Insulin = float(request.form['Insulin'])
    bmi = float(request.form['BMI'])
    dpf = float(request.form['diabetespedigreefunction'])
    age = float(request.form['age'])

    # Pass the form data to the machine learning model for prediction
    input_data = [[pregnancies, glucose, bp, skin, Insulin, bmi, dpf, age]]
    # input_data = [[1,	90,	70,	29,	0,	27.5,	0.4, 31]]

    Diabetes_classifier = pickle.load(open("./SavedModel/Diabetes_classifier", 'rb'))
    prediction = Diabetes_classifier.predict(input_data)
    # print(prediction)

    # if (prediction[0] == '0'):
    #     return ('The person is not diabetic')
    # else:
    #     return ('The person is diabetic')

    return render_template('test_result.html',Disease='Diabetes', Result=prediction[0])





# ******* this is for Heart_Disease_Prediction ******* 
@app.route('/Heart_Disease_Prediction', methods=['POST'])
def Heart_Disease_Prediction():
     
    # Get the form data from the request object
    age = float(request.form['age'])
    sex = float(request.form['sex'])
    cp = float(request.form['cp'])
    trestbps = float(request.form['trestbps'])
    chol = float(request.form['chol'])
    fbs = float(request.form['fbs'])
    restecg = float(request.form['restecg'])
    thalach = float(request.form['thalach'])
    exang = float(request.form['exang'])
    oldpeak = float(request.form['oldpeak'])
    slope = float(request.form['slope'])
    ca = float(request.form['ca'])
    thal = float(request.form['thal'])
    
    # Pass the form data to the machine learning model for prediction
    input_data = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
    # input_data = [[62,0,0,140,268,0,0,160,0,3.6,0,2,2]]
    
    Hear_Disease_classifier = pickle.load(open("./SavedModel/Hear_Disease_classifier", 'rb'))
    
    prediction = Hear_Disease_classifier.predict(input_data)
    # print(prediction)

    # if (prediction[0] == '0'):
    #     return ('The person does not have a Heart Disease')
    # else:
    #     return ('The person has Heart Disease')

    return render_template('test_result.html',Disease='Heart', Result=prediction[0])





if __name__ == '__main__':
	app.run(debug = True)