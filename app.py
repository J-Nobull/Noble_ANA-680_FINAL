from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load model
model = joblib.load('Final.pkl')

# Questions for form
questions = {
    'work_interfere_3': "If you have a mental health condition, do you feel that it OFTEN interferes with your work?",
    'work_interfere_2': "If you have a mental health condition, do you feel that it SOMETIMES interferes with your work?",
    'family_history_1': "Do you have family with a history of mental illness?",
    'work_interfere_1': "If you have a mental health condition, do you feel that it NEVER interferes with your work?",
    'Gender_2': "Do you identify as the sex you were born?",
    'care_options_1': "Do you know the options for mental health care your employer provides?",
    'Gender_1': "Is your Gender Female?",
    'benefits_1': "Does your employer provide mental health benefits?",
    'coworkers_1': "Would you be willing to discuss a mental health issue with your coworkers?",
    'leave_4': "Is it VERY DIFFICULT for you to take medical leave for a mental health condition?",
    'leave_3': "Is it SOMEWHAT DIFFICULT for you to take medical leave for a mental health condition?",
    'mental_health_interview_1': "Would you bring up a mental health issue with a potential employer in an interview?",
    'seek_help_1': "Does your employer provide resources to learn more about mental health issues and how to seek help?"
}

@app.route('/')
def home():
    return render_template('index.html', questions=questions)

@app.route('/predict_form', methods=['POST'])
def predict_form():
    try:
        input_values = [int(request.form.get(key)) for key in questions]
        features = np.array(input_values).reshape(1, -1)
        prediction = model.predict(features)[0]
        return render_template('result.html', prediction=int(prediction))
    except Exception as e:
        return f"Error during prediction: {e}"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        features = np.array(data['features']).reshape(1, -1)
        prediction = model.predict(features)[0]
        return jsonify({'prediction': int(prediction)})
    except Exception as e:
        return jsonify({'error': str(e)})

