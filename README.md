# Financial Machine Learning

## Table of Contents

- [About](#about)
- [Financial APIs](#apis)
- [Resources](#res)

## About <a name = "about"></a>

This is a Financial Machine Learning Project for trading.

## Financial APIs to request stock quotes and historical data information <a name = "apis"></a>


| API        | Positive things           | Negative things  |
| ------------- |:-------------:| -----:|
| [Alpaca](https://docs.alpaca.markets/)      | Rate limit: 200/min<br>Play with fake money | - |
| [WordTradingData](https://www.worldtradingdata.com/documentation)      | -      |  - |
| [Intrinio](https://docs.intrinio.com/documentation/api_v2/limits) | - | - |
| [Alpha Vantage](https://www.alphavantage.co) | - | - |
| [IEX Cloud](https://www.iexcloud.io/api/#introduction) | Rate limit: 1/10ms | - |
| [Polygon](https://www.polygon.io) | - | - |
| [Traider](https://www.developer.traider.com) | - | - |


## Resources <a name =  "res"></a>

Marcos Prado Website: http://www.quantresearch.org/

## Requests for datasets 

### From 20 years ago till now with a step of 1 day:

First you must to get your apiKey from https://www.alphavantage.co/support/#api-key
Then execute the next line in your terminal replacing "demo" with your apikey generated.

```
curl 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MELI&outputsize=full&apikey=demo&datatype=csv' > data.csv
```
