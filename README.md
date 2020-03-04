# Web Api Converter Request

First, open the commando prompt.

Then you need to clone the git repository:
```
$ git clone git@github.com:dottiOliviero/WebApi.git
```
Or:
```
$ git clone https://github.com/dottiOliviero/WebApi.git
```

Then change into the WebApi folder:

```
$ cd WebApi
```

Now, you need to create a virtual environment
and install all the required packages listed in the *requirements.txt* file

You can use pip+virtualenv:
```
$ pip install virtualenv  #in case you don't have it 
$ virtualenv venv
$ .venv/bin/activate # on Windows use "venv\Scripts\activate"
$ pip install -r requirements.txt
```

## Run the example

To run the application you need to setup Flask. In the command prompt type the following commands:
```
$ export FLASK_APP = main.py  # on Windows use "set FLASK_APP=main.py"
$ flask run
```

you can see from your console that the application is running on http://127.0.0.1:5000.

Open a browser and type http://127.0.0.1:5000, it appears a blank page which says "Welcome to the currency converter".

To perform a value conversion, you have to indicate the amount, the source currency (src_currency), the destination currency (dest_currency) and the reference time for the change rate (reference_date).
The endpoint is called _convert_, hence the call to the source code should have the following structure:

http://127.0.0.1:5000/convert/amount=10&src_currency=EUR&dest_currency=JPY&reference_date=2020-02-17

for example this request will return the following json:

```
{
  "amount": 1190.5, 
  "currency": "JPY"
}
```

_it is important_ to format the reference date in this way (YYYY-MM-DD).
