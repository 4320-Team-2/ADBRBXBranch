import requests as rq
import json
import pygal
import Constants
import date
import lxml

#Selecting the time series function, company symbol, and how big the output size
#will be, and our API key.
data = {
    "function":Constants.TIME_SERIES,
    "symbol":Constants.SYMBOL,
    "outputsize":"full",
    "apikey":Constants.API_KEY
    }

#Sending our request to the API using the information we put in data
apiCall = rq.get(Constants.API_URL, params=data)

#Stores the json-enconded content in the retrieved data.
response = apiCall.json()

#Retriving the dates in putting them into a dictonary.
dates = []
[dates.append(date) for date in response["Time Series (Daily)"]]

set_2 = frozenset(date.date_strings)

final_dates = [x for x in dates if x in set_2]

final_dates.reverse()

#Creating a tuple of the dates so we can use them as key.
key = tuple(final_dates)

#Populating lists with data from API
opens = []
for x in range(len(key)):
    opens.append(response["Time Series (Daily)"][key[x]]["1. open"])
    
highs = []
for x in range(len(key)):
    highs.append(response["Time Series (Daily)"][key[x]]["2. high"])
    
lows = []
for x in range(len(key)):
    lows.append(response["Time Series (Daily)"][key[x]]["3. low"])
    
closes = []
for x in range(len(key)):
    closes.append(response["Time Series (Daily)"][key[x]]["4. close"])
    
#Dumb Stuff Down Here, converting list of strings to list of floats so we can plot them
floatOpen = [float(i) for i in opens]
floatHigh = [float(i) for i in highs]
floatLow = [float(i) for i in lows]
floatCloses = [float(i) for i in closes]

#If true, prints line chart. Else prints the bar chart.
if Constants.CHART_TYPE == True:
    chart = pygal.Line()
    chart.x_labels = final_dates
    chart.title = "Stock Date for " + Constants.SYMBOL + ": " + Constants.START_DATE + " to " + Constants.END_DATE
    chart.add("Open",floatOpen)
    chart.add("High",floatHigh)
    chart.add("Low", floatLow)
    chart.add("Close",floatCloses)
    chart.render_in_browser()
    print("Success!")
else:
    chart = pygal.Bar()
    chart.x_labels = final_dates
    chart.title = "Stock Date for " + Constants.SYMBOL + ": " + Constants.START_DATE + " to " + Constants.END_DATE
    chart.add("Open",floatOpen)
    chart.add("High",floatHigh)
    chart.add("Low", floatLow)
    chart.add("Close",floatCloses)
    chart.render_in_browser()
    print("Success!")
