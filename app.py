from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model
model = joblib.load('Final.pkl')

@app.route('/')
def home():
    return 'Mental Health Treatment Prediction API is running!'

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        features = np.array(data['features']).reshape(1, -1)

        # Debug: print received input
        print(f"Received features: {features}")

        prediction = model.predict(features)[0]
        return jsonify({'prediction': int(prediction)})

    except Exception as e:
        # Debug: print error to terminal
        print(f"Prediction error: {e}")
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
