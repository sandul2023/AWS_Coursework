from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/price', methods=['GET'])
def get_price():
    # Mock response for simplicity
    return jsonify({"price": "1000 USD"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)
