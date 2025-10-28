from flask import Flask, request, jsonify
import json

app = Flask(__name__)
DATA_FILE = 'customers.json'

def read_customers():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def write_customers(customers):
    with open(DATA_FILE, 'w') as f:
        json.dump(customers, f, indent=2)

@app.route('/customers', methods=['POST'])
def add_customer():
    customers = read_customers()
    new_customer = request.json
    new_customer['id'] = max([c['id'] for c in customers], default=0) + 1
    customers.append(new_customer)
    write_customers(customers)
    return jsonify(new_customer), 201

@app.route('/customers', methods=['GET'])
def get_customers():
    customers = read_customers()
    return jsonify(customers)

@app.route('/customers/<int:id>', methods=['GET'])
def get_customer(id):
    customers = read_customers()
    customer = next((c for c in customers if c['id'] == id), None)
    if not customer:
        return jsonify({"message": "Customer not found"}), 404
    return jsonify(customer)

@app.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    customers = read_customers()
    customer = next((c for c in customers if c['id'] == id), None)
    if not customer:
        return jsonify({"message": "Customer not found"}), 404
    data = request.json
    customer.update(data)
    write_customers(customers)
    return jsonify(customer)

@app.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    customers = read_customers()
    filtered = [c for c in customers if c['id'] != id]
    if len(filtered) == len(customers):
        return jsonify({"message": "Customer not found"}), 404
    write_customers(filtered)
    return jsonify({"message": "Customer deleted"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
