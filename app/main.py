from flask import Flask
from flask import make_response
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/fib-generator', methods=['GET'])
def fib_generator_page():
    error = None
    fib_max_number = request.args.get('fib-max-number')

    try:
        fib_max_number = int(request.args.get('fib-max-number'))
    except ValueError as e:
        return render_template('error_page.html', error=e)

    if fib_max_number > 0:
        fib_list = [n for n in _fibonacci(fib_max_number)]
        return render_template('fib_generator.html',
                               error=error,
                               fib_sequence=fib_list,
                               fib_max_number=fib_max_number)
    else:
        error = "Must provide a number greater than 0"
        response = make_response(
            render_template('error_page.html', error=error), 404)
        return response

@app.errorhandler(404)
def not_found(error):
    return render_template('error_page.html'), 404

def _fibonacci(fib_max_number):
    x, y = 0, 1
    while x < fib_max_number:
        yield x
        x, y = y, x + y

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
