from flask import Flask, request, render_template, flash, redirect, url_for
# from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes

app = Flask(__name__)

app.config['SECRET_KEY'] = "chickenzarecool21837"
# debug = DebugToolbarExtension(app)



@app.route('/')
def show_form():
    """Shows greeter V1 Form"""
    return render_template("form.html")


@app.route('/result', methods=['GET', 'POST'])
def get_greeting():
    Currency = request.form['Currency']
    Currency2 = request.form['Currency2']
    Amount = request.form.get('Amount', type=float)
    error = False
    print(Currency2)
    print(Currency)
    print(Amount)

    c = CurrencyRates()
    codes = CurrencyCodes()
    symbol = codes.get_symbol(Currency2)
    symbol1 = codes.get_symbol(Currency)

    if Amount is None:
        flash('Please enter a valid amount!')
        error = True
    if symbol is None:
        flash(f'Invalid currency code: {Currency2}') 
        error = True
    if symbol1 is None:
        flash(f'Invalid currency code: {Currency}') 
        error = True

        
    if error:
        return redirect(url_for('show_form'))

    conversion = c.convert(Currency, Currency2, Amount)
    return render_template("greet.html", Amount=conversion,
                                         symbol=symbol)

