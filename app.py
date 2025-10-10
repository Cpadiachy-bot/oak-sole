from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

YOCO_SECRET_KEY = "pk_test_b979d408P4KP9J47bd44"  # put your secret key here

@app.route('/charge', methods=['POST'])
def charge():
    data = request.get_json()
    token = data.get('token')
    amount = data.get('amount')  # in cents

    response = requests.post(
        "https://online.yoco.com/v1/charges/",
        headers={"X-Auth-Secret-Key": YOCO_SECRET_KEY},
        json={"token": token, "amountInCents": amount, "currency": "ZAR"}
    )
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(port=5000, debug=True)
