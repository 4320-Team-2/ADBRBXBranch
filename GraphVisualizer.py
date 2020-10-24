import requests as rq
import json
import pygal

#URL to Alphavantage API
API_URL = "https://www.alphavantage.co/query"

#Selecting the time series function, company symbol, and how big the output size will be, and our API key.
data = {
    "function":"TIME_SERIES_DAILY",
    "symbol":"IBM",
    "outputsize":"compact",
    "apikey":"SPFP6JN8KMDZ9IPM"
    }

#Sending our request to the API using the information we put in data
apiCall = rq.get(API_URL, params=data)

#Stores the json-enconded content in the retrieved data.
response = apiCall.json()


#Retriving the dates in putting them into a dictonary.
dates = []
[dates.append(date) for date in response["Time Series (Daily)"]]
#print(dates)

#Creating a tuple of the dates so we can use them as key.
key = tuple(dates)

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

#Graphing data from lists, creates a .svg file you can view in whatever folder this file is in.
line_chart = pygal.Line()
line_chart.x_labels = dates
line_chart.add("Open",floatOpen)
line_chart.add("High",floatHigh)
line_chart.add("Low", floatLow)
line_chart.add("Close",floatCloses)
line_chart.render_to_file("testing.svg")
print("Success!")
