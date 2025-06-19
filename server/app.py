#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>', 200


@app.route('/print/<parameter>')
def print_parameter(parameter):
    print(parameter)
    return parameter, 200


@app.route('/count/<int:parameter>')
def count(parameter):
    output = '\n'.join(str(i) for i in range(parameter)) + '\n'
    return output, 200


@app.route('/math/<int:num1>/<op>/<int:num2>')
def math(num1, op, num2):
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == 'div':
        result = num1 / num2
    elif op == '%':
        result = num1 % num2
    else:
        result = "Invalid operation"
    return str(result), 200


if __name__ == '__main__':
    app.run(port=5555, debug=True)
