import pickle
# *********** Prediction ***********
Hear_Disease_classifier = pickle.load(open("../SavedModel/Hear_Disease_classifier", 'rb'))

input_data = [[62,0,0,140,268,0,0,160,0,3.6,0,2,2]]
prediction = Hear_Disease_classifier.predict(input_data)
# print(prediction)

if (prediction[0] == '0'):
    print('The person does not have a Heart Disease')
else:
    print('The person has Heart Disease')