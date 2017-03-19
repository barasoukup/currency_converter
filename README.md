Currency converter
==================

Currency convertor as a homework for kiwi.com. Program converts amount from input currency into output currency.

## Installation

Script uses Python 2.7 and its libraries: requests, json, sys, getopt. If your Python installation does not include any of them, install them using pip.
Copy currency_converter.py and symbols.py into same folder.

## Usage

Run from command line with following parameters:

```
currency_converter.py --amount <float> --input_currency <3 letter currency code or symbol> --output_currency <3 letter currency code or symbol>
```

- --amount - amount which we want to convert - float
- --input_currency - input currency - 3 letters name or currency symbol
- --output_currency - requested/output currency - 3 letters name or currency symbol

Parameters amount and input_currency are required. If output_currency param is missing, amount will be converted to all known currencies.

## Output

- json with following structure.
```
{
    "input": { 
        "amount": <float>,
        "currency": <3 letter currency code>
    }
    "output": {
        <3 letter currency code>: <float>
    }
}
```
