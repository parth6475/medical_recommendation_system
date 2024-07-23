import pickle
# *********** Prediction ***********
# input_data = [[6, 167, 73, 20, 176, 26.9, 0.588, 52]]
input_data = [[1,	90,	70,	29,	0,	27.5,	0.4, 31]]

Diabetes_classifier = pickle.load(open("../SavedModel/Diabetes_classifier", 'rb'))
prediction = Diabetes_classifier.predict(input_data)
# print(prediction)

if (prediction[0] == '0'):
    print('The person is not diabetic')
else:
    print('The person is diabetic')