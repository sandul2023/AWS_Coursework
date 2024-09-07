from flask import Flask, jsonify 

app = Flask(__name__)


@app.route('/account/<username>', methods=['GET'])
def get_account(username):
    # Mock response for simplicity
    return jsonify({"username": username, "status": "Active"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002, debug=True)
