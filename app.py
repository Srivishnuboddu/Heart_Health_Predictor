from flask import Flask, render_template, request
import pickle
import pandas as pd
import os

app = Flask(__name__)

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Function to get remedies based on prediction percentage
def get_remedies(probability):
    if 40 <= probability < 50:
        return ["Regular exercise", "Healthy diet", "Routine check-ups"]
    elif 50 <= probability < 60:
        return ["Consult a cardiologist", "Include heart-healthy foods", "Monitor blood pressure"]
    elif 60 <= probability < 70:
        return ["Medication as prescribed", "Increase physical activity", "Limit salt intake"]
    elif 70 <= probability < 80:
        return ["Strict dietary control", "Daily monitoring", "Stress management"]
    elif 80 <= probability < 90:
        return ["Specialist care", "Cardiac rehabilitation", "Potential surgical intervention"]
    else:
        return ["Immediate medical attention", "Advanced treatment", "Lifestyle changes under supervision"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            age = int(request.form['age'])
            restbp = float(request.form['restbp'])
            chol = float(request.form['chol'])
            maxhr = float(request.form['maxhr'])
            oldpeak = float(request.form['oldpeak'])
            slope = int(request.form['slope'])
            ca = int(request.form['ca'])
            thal = request.form['thal']

            input_data = pd.DataFrame([[age, restbp, chol, maxhr, oldpeak, slope, ca, thal]],
                                      columns=['Age', 'RestBP', 'Chol', 'MaxHR', 'Oldpeak', 'Slope', 'Ca', 'Thal'])

            input_data = pd.get_dummies(input_data, columns=['Thal', 'Slope'], drop_first=True)
            model_columns = list(model.feature_names_in_)
            input_data = input_data.reindex(columns=model_columns, fill_value=0)

            prediction_probability = model.predict_proba(input_data)[0][1] * 100
            if prediction_probability < 40:
                result = 'Heart is Healthy!'
                remedies = None
            else:
                result = f'{prediction_probability:.2f}% likelihood of Heart Disease.'
                remedies = get_remedies(prediction_probability)

            return render_template('predict.html', prediction_text=f'Result: {result}', remedies=remedies)
        except Exception as e:
            return f"Error: {str(e)}"

    return render_template('predict.html')

if __name__ == '__main__':
    # app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
