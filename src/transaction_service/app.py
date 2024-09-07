from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/transaction', methods=['POST'])
def create_transaction():
    # Mock response for simplicity
    return jsonify({"status": "Transaction Created"}), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
