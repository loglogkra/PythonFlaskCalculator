from flask import Flask, render_template, url_for, request
app = Flask(__name__)


@app.route('/')
def calculator():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    result = str(data[0])
    for i in range(1, len(data), 2):
        operator = data[i]
        operand = data[i+1]
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
    return result


if __name__ == '__name__':
    app.run(debug=True)
