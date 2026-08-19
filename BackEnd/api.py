from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('extra_tree_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        tv = data.get('TV', 0.0)
        radio = data.get('Radio', 0.0)
        newspaper = data.get('Newspaper', 0.0)
        
        input_data = np.array([[tv, radio, newspaper]])
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)
        
        return jsonify({
            'status': 'success',
            'predicted_sales': float(prediction[0])
        })
        
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)