from flask import Flask, jsonify, request
import requests
import xmltodict

app = Flask(__name__)

# function that respond to the get request
@app.route('/convert/amount=<amount>&src_currency=<src_currency>&dest_currency=<dest_currency>&reference_date=<reference_date>', methods = ['GET'])
def get_converted_currency(amount,src_currency,dest_currency,reference_date):
    l = load_exchanges_rates()
    src_curr_value, dest_curr_value, found = get_currencies(l,reference_date,src_currency,dest_currency)
    if found:
        current_value = (dest_curr_value/src_curr_value)*float(amount)
        return jsonify({'amount': current_value, 'currency': dest_currency}), 200
    else:
        return jsonify({"no available data for the required reference data {0}".format(reference_date)}), 404


# function that loads the exchange rates from the ecb site
def load_exchanges_rates():
    url = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml'
    r = requests.get(url)
    d = dict(xmltodict.parse(r.text))
    l = d['gesmes:Envelope']['Cube']['Cube']
    return l

#default home function
@app.route('/')
def greeting():
    return "Welcome to the currency converter"

# function that returns the currency rate values for the desired date and currencies
def get_currencies(currency_list,reference_date,src_currency,dest_currency):
    print(reference_date,src_currency,dest_currency)
    src_currency_date = 1
    dest_currency_date = 1
    found = False
    for i in range(len(currency_list)):
        if currency_list[i]['@time'] == str(reference_date):
            found = True
            for item in currency_list[i]['Cube']:
                if item['@currency'] == src_currency:
                    src_currency_date = item['@rate']
                if item['@currency'] == dest_currency:
                    dest_currency_date = item['@rate']

    return float(src_currency_date), float(dest_currency_date), found
