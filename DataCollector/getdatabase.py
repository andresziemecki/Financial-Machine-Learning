import requests
import datetime
import time
import sys

# Introduce your parameters
token = '' # token of IEX Cloud
symbol = 'meli' # symbol of the market in lower case, for example "meli" for MercadoLibre
yearsBefore = 1 # up to one

""" Request Format
response = requests.get(
    'https://cloud.iexapis.com/stable/stock/meli/chart/date/20190421',
    params={'format':'csv',
            'token':'Your Token'},
)
"""

# Get date from today
today = datetime.datetime.now()
todayDay = today.strftime("%d")
todayMonth = today.strftime("%m")
todayYear = today.strftime("%Y")

# Check for 29th of Febrary, because this may couse errors
if todayDay == 29 and todayMonth == 2:
    todayDay = '28'
    todayMonth = '2'

date = datetime.datetime( int(todayYear) - yearsBefore, int(todayMonth), int(todayDay))
csvFile = open("data.csv", "w")
iteration = 0

# Request data till today
while not (date.strftime("%Y") == todayYear and date.strftime("%m") == todayMonth and date.strftime("%d") == todayDay) : 
    
    # Set params day of the request
    dateDay = date.strftime("%d")
    dateMonth = date.strftime("%m")
    dateYear = date.strftime("%Y")

    # Log the date of the request
    print(dateYear, dateMonth, dateDay)

    # construct the request
    URL = 'https://cloud.iexapis.com/stable/stock/'+ symbol +'/chart/date/' + dateYear + dateMonth + dateDay 
    params={'format':'csv',
            'token':token}

    # Do the request
    i = 0
    while True:
        time.sleep(1)
        response = requests.get(URL, params=params,)
        if(response.status_code == 200 or i > 2):
            break
        elif i > 2:
            sys.exit("Error - Program finished - Status code :" + str(response.status_code))
        else:
            i = i + 1
    
    # update request day
    date = date + datetime.timedelta(days=1)

    # check for empty content of the request 
    if len(response.text) == 0:
        continue

    # If it is the first iteration write the header, otherwise ommit it
    if iteration == 0:
        tmp = response.text
        iteration = iteration + 1    
    else:
        tmp = '\n'.join(response.text.split('\n')[1:])
    
    # Write the content
    n = csvFile.write(tmp + '\n')
    csvFile.flush()

# end
csvFile.close()

