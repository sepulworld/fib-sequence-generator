from flask import Flask, request, make_response, render_template

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
        app.logger.info("Max number to calculate fib seq to: {}"
                        .format(fib_max_number))
    except ValueError as e:
        app.logger.error("Failure to set fib_max_number as int: {}".format(e))
        return render_template(
            'error_page.html',
            error="Not an integer! '{}'".format(fib_max_number))

    if fib_max_number > 0:
        fib_list = [n for n in _fibonacci(fib_max_number)]
        app.logger.info("Fib list to be rendered {}".format(fib_list))
        return render_template('fib_generator.html',
                               error=error,
                               fib_sequence=fib_list,
                               fib_max_number=fib_max_number)
    else:
        error = "Must provide a number greater than 0"
        app.logger.error("{}".format(error))
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
