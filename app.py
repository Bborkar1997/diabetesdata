from flask import Flask,jsonify,render_template,request
from utils import Diabetes
app =Flask(__name__)
@app.route("/home")
def home():

    return render_template('index.html')

@app.route("/diabetes",methods = ['GET','POST'])
#@app.route('/predict_charges', methods = ['GET','POST'])
def diabetes():
    if request.method == 'POST':
        data = request.form.get

        #data= request.form
        print("Used data is:",data)
        Glucose= eval(data('Glucose'))
        BloodPressure =eval(data('BloodPressure'))
        SkinThickness =eval(data('SkinThickness'))
        Insulin =eval(data('Insulin'))
        BMI=eval(data('BMI'))
        DiabetesPedigreeFunction =eval(data('DiabetesPedigreeFunction'))
        Age =eval(data('Age'))

        diabetes_pred = Diabetes()
        dia_pred=diabetes_pred.get_diabetes(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
        #return jsonify({"Result:":f"the predicted diabetes class is {dia_pred}"})
        return render_template('index.html',dia_class_pred = dia_pred)
        print("the print class is",dia_pred)

@app.route("/addition")
def addition():
    a = 10
    b = 20
    add = a+b
    print(f"The addition of {a} and {b} is {add} ")
    return f"The addition of {a} and {b} is {add} "
if __name__ == ("__main__"):
    app.run()