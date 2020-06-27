from flask import Flask, render_template, request, redirect

app = Flask(__name__)


def fibonacci(n):
    n_1, n_2 = 1, 0
    for i in range(n):
        n_1, n_2 = n_2, n_1 + n_2
    return n_2


@app.route('/fibonacci/<number>', methods=['GET'])
def fibonacci_element(number):
    try:
        number = int(number)
        return str(fibonacci(number))
    except Exception as err:
        print(err)
        return "Input Error"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form
        number = data['fnumber']
        return redirect('/fibonacci/{}'.format(number))
    else:
        return render_template('textbox.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
