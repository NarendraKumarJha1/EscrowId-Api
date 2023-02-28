from flask import Flask, jsonify, request

app = Flask(__name__)

digit = 0

@app.route('/digit', methods=['GET'])
def get_digit():
    return jsonify({'digit': digit})

@app.route('/digit', methods=['POST'])
def update_digit():
    global digit
    digit = request.json['digit']
    return jsonify({'digit': digit})

if __name__ == '__main__':
    app.run()
