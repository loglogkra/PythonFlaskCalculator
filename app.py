from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def calculator():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    # prevent unwanted JSON chars
    result = str(data[0])
    if not validate_string(result):
        return 'Error'

    try:
        for i in range(1, len(data), 2):
            operator = data[i]
            operand = data[i + 1]
        if operator == '+':
            result += ' + ' + str(operand)
            result = str(eval(result))
        elif operator == '-':
            result += ' - ' + str(operand)
            result = str(eval(result))
        elif operator == '*':
            result += ' * ' + str(operand)
            result = str(eval(result))
        elif operator == '%':
            result += ' % ' + str(operand)
            result = str(eval(result))
        else:
            result = 0
        return result
    except ValueError:
        return 'Err'
    except TypeError:
        return 'Err'


def validate_string(s):
    valid_chars = set("012345789.+-%*")
    return all(char in valid_chars for char in s)


if __name__ == '__name__':
    app.run(debug=True)
