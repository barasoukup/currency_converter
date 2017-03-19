# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:16:49 2017

@author: matej

Currency converter, more info:
https://github.com/matejsoukup/currency_converter

"""

import requests
import json
import sys, getopt
from symbols import symbols

def convert(amount,input_currency,output_currency=None):
    currency_dict=symbols
    
    if input_currency in currency_dict:         #if symbol is in dictionary, replace it
        input_currency=currency_dict[input_currency]

    http='http://api.fixer.io/latest?base='+input_currency      #url for all currencies, free API
    
    if output_currency:
        if output_currency in currency_dict:
            output_currency=currency_dict[output_currency]
        http+='&symbols='+output_currency                       #url for one currency

    r = requests.get(http)
    if r.status_code==200:                                      #if request is OK
        if any(r.json()['rates']):                              #rates returned, good inputs
            res={"input":{"amount":amount, "currency": input_currency},"output":{}}
            for currency in r.json()['rates']:                  #put every returned currency into output
                res["output"][currency]=round(r.json()['rates'][currency]*amount,2)
            return json.dumps(res, indent=4,ensure_ascii=False,sort_keys=True)          #returned json
        else:
            raise ValueError("Unknown output currency")         
    elif r.status_code==422:
        raise ValueError("Unknown input currency")
    else:
        raise RuntimeError("Request error")

def main(argv):
    amount,input_currency,output_currency=None,None,None
    opts, args = getopt.getopt(argv,"",["amount=","input_currency=","output_currency="])
    for opt, arg in opts:
        if opt == '--amount':                                   #load amount
            try:
                amount=float(arg)
            except:
                raise ValueError("wrong amount, should be float")
        elif opt == '--input_currency':                         #load input currency
            input_currency=arg.decode(sys.getfilesystemencoding())
        elif opt == '--output_currency':                        #load ouput currency
            output_currency=arg.decode(sys.getfilesystemencoding())
  
    if (amount and input_currency):
        print convert(amount,input_currency,output_currency)
    else:                                                       #if amount and input currency are not set raise exception
        raise Exception("amount and input currency must be filled")

if __name__ == "__main__":
    try:
       main(sys.argv[1:])
    except Exception as e:
        print "ERROR:",e
        print 'currency_converter.py --amount <float> --input_currency <3 letter currency code or symbol> --output_currency <3 letter currency code or symbol>'
        sys.exit(1)
   

    
        
    
