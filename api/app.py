from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database for demonstration purposes
dispensers = {
    1: {"name": "Tap 1", "status": "off"},
    2: {"name": "Tap 2", "status": "off"},
}


@app.route('/dispensers', methods=['GET'])
def get_dispensers():
    return jsonify(dispensers)


@app.route('/dispensers/<int:dispenser_id>', methods=['GET'])
def get_dispenser(dispenser_id):
    dispenser = dispensers.get(dispenser_id)
    if dispenser:
        return jsonify(dispenser)
    return jsonify({"error": "Dispenser not found"}), 404


@app.route('/dispensers/<int:dispenser_id>', methods=['PUT'])
def update_dispenser(dispenser_id):
    dispenser = dispensers.get(dispenser_id)
    if dispenser:
        data = request.get_json()
        dispenser['status'] = data.get('status', dispenser['status'])
        return jsonify(dispenser)
    return jsonify({"error": "Dispenser not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
