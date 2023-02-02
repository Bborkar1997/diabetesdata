import pickle
import json
import numpy as np

class Diabetes():
    def __init__(self):
        with open("knn_classifire.pkl","rb") as f:
            self.model =pickle.load(f)
            print("self.model>>",self.model)

    def get_diabetes(self,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):

        test_array = np.array([Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age],ndmin = 1)
        print("The test array is:",test_array)
        predicted_diabetes = self.model.predict([test_array])[0]
        print("The predicted diabetes is", predicted_diabetes)
        return predicted_diabetes