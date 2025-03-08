from flask import Flask, jsonify, request
import os

app = Flask(__name__)

#route defined
@app.route('/')
def home():
    return "API is running!"

if __name__ == '__main__':
    app.run(debug=True)

    
# Sample endpoint to process data
@app.route('/process', methods=['POST'])
def process_data():
    data = request.json
    return jsonify({"message": "Data processed successfully!", "data": data})

# Sample endpoint to trigger an alert
@app.route('/send-alert', methods=['GET'])
def send_alert():
    return jsonify({"alert": "System health is critical!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
