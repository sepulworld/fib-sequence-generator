from flask import Flask, request, make_response, render_template

app = Flask(__name__)

@app.route('/')
def index_page():
    """Generate index page which will display
    an input for fib sequence generator
    """
    return render_template('index.html')

@app.route('/fib-generator', methods=['GET'])
def fib_generator_page():
    """Generate a page that displays results of provided 'fib-max-number'
    from the index page
    """
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
    """Render an error page. Used when a non-integer or a number equal to or
    less than zero is inputted
    """
    return render_template('error_page.html'), 404

def _fibonacci(fib_max_number):
    """Calculate the Fibonacci sequence up to the given fib_max_number vaule
    the yeild of x is the next number in ths loop that is the addition of the 2
    previous numbers
    """
    x, y = 0, 1
    while x < fib_max_number:
        yield x
        x, y = y, x + y

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
