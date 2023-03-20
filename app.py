from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def calculator():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    # prevent unwanted JSON from frontend
    result = str(data[0])
    if not validate_input(result):
        return 'Invalid Input!'

    try:
        i = 1
        while i < len(data):
            operator = data[i]
            operand = data[i + 1]
            if operator == '+':
                result += ' + ' + str(operand)
            elif operator == '-':
                result += ' - ' + str(operand)
            elif operator == '*':
                result += ' * ' + str(operand)
            elif operator == '%':
                result += ' / ' + str(operand)
            i += 2
        result = str(eval(result))
        return result
    except:
        return 'Unknown Exception'


def validate_input(s):
    valid_chars = set("012345789.+-%*")
    return all(char in valid_chars for char in s)


if __name__ == '__name__':
    app.debug = True
    app.run
