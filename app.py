from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# # Handling GET request
@app.route('/data', methods=['GET'])
def get_data():
    return jsonify({
        "id": "1",
        "name": "Jeje",
        "age": 19
    })

# Handling POST request
@app.route('/data', methods=['POST'])
def post_data():
    data = request.json
    return jsonify({
        "data-received": True,
        "data": data
    })

# # Handling PUT request
@app.route('/data/<int:id>', methods=['PUT'])
def put_data(id):
    data = request.json
    return jsonify({"message": f"Data with ID {id} updated", "updated_data": data})

# # Handling DELETE request
@app.route('/data/<int:id>', methods=['DELETE'])
def delete_data(id):
    return jsonify({"message": f"Data with ID {id} deleted"})


if __name__ == '__main__':
    app.run(debug=True, port=8000)