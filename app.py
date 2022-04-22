from flask import  Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route("/predict", methods = ['GET', 'POST'])
def predict():
    if request.method == 'POST':
        print(request.form.get("Age"))
        print(request.form.get("RestingBP"))
        print(request.form.get("Cholesterol"))
        print(request.form.get("FastingBS"))
        print(request.form.get("MaxHR"))
        print(request.form.get("OldPeak"))
        print(request.form.get("Sex_F"))
        print(request.form.get("Sex_M"))
        print(request.form.get("ChestPainType_ASY"))
        print(request.form.get("ChestPainType_ATA"))
        print(request.form.get("ChestPainType_NAP"))
        print(request.form.get("ChestPainType_TA"))
        print(request.form.get("RestingECG_LVH"))
        print(request.form.get("RestingECG_Normal"))
        print(request.form.get("RestingECG_ST"))
        print(request.form.get("ExerciseAngina_N"))
        print(request.form.get("ExerciseAngina_Y"))
        print(request.form.get("ST_Slope_Down"))
        print(request.form.get("ST_Slope_Flat"))
        print(request.form.get("ST_Slope_Up"))
        try:
            Age = float(request.form["Age"])
            RestingBP = float(request.form["RestingBP"])
            Cholesterol = float(request.form["Cholesterol"])
            FastingBS = float(request.form["FastingBS"])
            MaxHR = float(request.form["MaxHR"])
            OldPeak = float(request.form["OldPeak"])
            Sex_F = float(request.form["Sex_F"])
            Sex_M = float(request.form["Sex_M"])
            ChestPainType_ASY = float(request.form["ChestPainType_ASY"])
            ChestPainType_ATA = float(request.form["ChestPainType_ATA"])
            ChestPainType_NAP = float(request.form["ChestPainType_NAP"])
            ChestPainType_TA = float(request.form["ChestPainType_TA"])
            RestingECG_LVH = float(request.form["RestingECG_LVH"])
            RestingECG_Normal = float(request.form["RestingECG_Normal"])
            RestingECG_ST = float(request.form["RestingECG_ST"])
            ExerciseAngina_N = float(request.form["ExerciseAngina_N"])
            ExerciseAngina_Y = float(request.form["ExerciseAngina_Y"])
            ST_Slope_Down = float(request.form["ST_Slope_Down"])
            ST_Slope_Flat = float(request.form["ST_Slope_Flat"])
            ST_Slope_Up = float(request.form["ST_Slope_Up"])
            pred_values = [Age, RestingBP, Cholesterol, FastingBS, MaxHR, OldPeak, Sex_F, Sex_M, ChestPainType_ASY, ChestPainType_ATA, ChestPainType_NAP, ChestPainType_TA, RestingECG_LVH, RestingECG_Normal, RestingECG_ST, ExerciseAngina_N, ExerciseAngina_Y, ST_Slope_Down, ST_Slope_Flat, ST_Slope_Up]
            pred_values_array = np.array(pred_values)
            pred_values_array = pred_values_array.reshape(1, -1)
            model_ = pickle.load(open('model.pkl', 'rb'))
            predictor = model_.predict(pred_values_array)
            if int(predictor) == 1:
                prediction = 'Heart Disease'
            else:
                prediction = 'No Heart Disease'
        except ValueError:
            return 'check your entries'
    return render_template('result.html', output = prediction)


if __name__ == "__main__":
    app.run(host='0.0.0.0')