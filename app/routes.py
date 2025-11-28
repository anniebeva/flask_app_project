from app import app

@app.route('/')
def home():
    return 'This is the homepage!'

@app.route('/hello')
def hello():
    return 'Hello, world!'

@app.route('/info')
def info():
    return 'This is an informational page'

@app.route('/calc/<int:num1>/<int:num2>')
def calc(num1: int, num2: int):
    try:
        total = int(num1) + int(num2)
        return f'The sum of {num1} and {num2} is {total}.'
    except ValueError:
        return f'Invalid format, enter numbers'

@app.route('/reverse/<text>')
def reverse(text: str):
    if text == '':
        return 'No text entered'
    return text[::-1]

@app.route('/user/<string:name>/<int:age>')
def greet_user(name: str, age: int):
    if name == '':
        return 'Enter name'

    try:
        age = int(age)
        if age < 0 or age > 123:
            return ('invalid age')

        return f'Hello, {name}. You are {age} years old'
    except ValueError:
        return 'Invalid format, enter age as a number'

