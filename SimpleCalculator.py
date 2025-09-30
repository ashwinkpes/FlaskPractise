from flask import Flask, request, jsonify
from calculator import Calculator

app = Flask(__name__)

@app.route('/', methods=['GET'])
def available_methods():
    """
    Returns a list of available calculator methods and their endpoints.
    """
    methods = {
        'sum': '/sum (POST, JSON: {"a": number, "b": number})',
        'difference': '/difference (POST, JSON: {"a": number, "b": number})',
        'product': '/product (POST, JSON: {"a": number, "b": number})',
        'quotient': '/quotient (POST, JSON: {"a": number, "b": number})',
        'percentage': '/percentage (POST, JSON: {"a": number, "b": number})'
    }
    return jsonify({
        'message': 'Welcome to the SimpleCalculator API!',
        'available_methods': methods
    })

@app.route('/sum', methods=['POST'])
def sum_route():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    result = Calculator.calculate_sum(a, b)
    return jsonify({'result': result})

@app.route('/difference', methods=['POST'])
def difference_route():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    result = Calculator.calculate_difference(a, b)
    return jsonify({'result': result})

@app.route('/product', methods=['POST'])
def product_route():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    result = Calculator.calculate_product(a, b)
    return jsonify({'result': result})

@app.route('/quotient', methods=['POST'])
def quotient_route():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    result = Calculator.calculate_quotient(a, b)
    return jsonify({'result': result})

@app.route('/percentage', methods=['POST'])
def percentage_route():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    result = Calculator.calculate_percentage(a, b)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
