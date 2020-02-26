# Financial Machine Learning

## Table of Contents

- [About](#about)
- [Financial APIs](#apis)
- [Resources](#res)

## About <a name = "about"></a>

This is a Financial Machine Learning Project for trading.

## Financial APIs <a name = "apis"></a>

Real time stcok quotes and historical data information.
https://docs.alpaca.markets/ -> posibility to play with ficticious money for backtesting.
https://www.worldtradingdata.com/documentation -> max daily request: 250
https://docs.intrinio.com/documentation/api_v2/limits -> 100 request per min
https://www.alphavantage.co -> max daily request 500. We can ask up to 20 yearss for historical data

## Resources <a name =  "res"></a>

Marcos Prado Website: http://www.quantresearch.org/

## Requests for datasets 

### From 20 years ago till now with a step of 1 day:

First you must to get your apiKey from https://www.alphavantage.co/support/#api-key
Then execute the next line in your terminal replacing "demo" with your apikey generated.

```
curl 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MELI&outputsize=full&apikey=demo&datatype=csv' > data.csv
```