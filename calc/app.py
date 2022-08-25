from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route('/add')
def do_add():
    """Add query parameters a and b"""
    a = int(request.args['a'])
    b = int(request.args['b']) 
    return str(add(a,b))

@app.route('/sub')
def do_sub():
    """Subtract query parameters a and b"""
    a = int(request.args['a'])
    b = int(request.args['b']) 
    return str(sub(a,b))

@app.route('/mult')
def do_mult():
    """Multiply query parameters a and b"""
    a = int(request.args['a'])
    b = int(request.args['b']) 
    return str(mult(a,b))

@app.route('/div')
def do_div():
    """Divide query parameters a and b"""
    a = int(request.args['a'])
    b = int(request.args['b']) 
    return str(div(a,b))

operations = {'add': add, 'sub': sub, "mult": mult, "div" : div}
@app.route('/math/<operation>')
def do_math(operation):
    """Perform operation add, sub, mult, or div on query parameters a and b."""

    a = int(request.args['a'])
    b = int(request.args['b']) 

    result = operations[operation](a,b)
    return str(result)
