from flask import Flask, jsonify, request

app = Flask(__name__)

data = {
    'value1': 0,
    'value2': 0
}


@app.route('/update', methods=['POST'])
def update_values():
    new_value1 = request.json.get('value1')
    new_value2 = request.json.get('value2')

    data['value1'] = new_value1
    data['value2'] = new_value2

    return jsonify({'message': 'Values updated successfully.'})


@app.route('/fetch', methods=['GET'])
def fetch_values():
    return jsonify(data)


if __name__ == '__main__':
    app.run()
