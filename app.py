from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'This is the homepage!'

@app.route('/hello')
def hello():
    return 'Hello, world!'

@app.route('/info')
def info():
    return 'This is an information page.'

@app.route('/calc/<num1>/<num2>')
def calc(num1: int, num2: int):
    try:
        total = int(num1) + int(num2)
        return f'The sum of {num1} and {num2} is {total}.'
    except ValueError:
        return f'Invalid format, enter numbers'

@app.route('/reverse/<text>')
def reverse(text):
    if text == '':
        return 'No text entered'
    return f'{text[::-1]}'

@app.route('/user/<name>/<age>')
def greet_user_w_age(name, age):
    if name == '':
        return 'Enter name'
    try:
        age = int(age)
        if age < 0 or age > 110:
            return 'Invalid age'

        return f'Hello, {name}. You are {age} years old.'
    except ValueError:
        return 'Invalid format, enter age as a number'


if __name__ == "__main__":
    app.run(debug=True)

