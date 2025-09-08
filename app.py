from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract values using correct form keys (all lowercase, matching HTML)
        age = int(request.form['age'])
        sex = int(request.form['sex'])
        chest_pain = int(request.form['cp'])
        resting_bp = int(request.form['trestbps'])
        cholesterol = int(request.form['chol'])
        fasting_bs = int(request.form['fbs'])
        resting_ecg = int(request.form['restecg'])
        max_hr = int(request.form['thalach'])
        exercise_angina = int(request.form['exang'])
        oldpeak = float(request.form['oldpeak'])
        st_slope = int(request.form['slope'])

        input_data = np.array([[age, sex, chest_pain, resting_bp, cholesterol, fasting_bs,
                                resting_ecg, max_hr, exercise_angina, oldpeak, st_slope]])
        prediction = model.predict(input_data)[0]

        if prediction == 0:
            result = 'The patient does not have heart disease.'
            result_class = 'text-success'
        else:
            result = 'The patient is likely to have heart disease. so please consult a doctor!..'
            result_class = 'text-danger'

        return render_template('index.html', prediction_text=result, result_class=result_class)

    except Exception as e:
        return f"Error occurred: {str(e)}", 400

if __name__ == '__main__':
    app.run(debug=True)
