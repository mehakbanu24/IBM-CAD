from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/get')
def get_method():
    return jsonify(message="GET Request Success"), 200
@app.route('/post', methods=['POST'])
def post_method():
    return jsonify(message="POST Request Success"), 201
@app.route('/notfound')
def not_found():
    return jsonify(error="Resource Not Found"), 404
if __name__ == '__main__':
    app.run(debug=True)
