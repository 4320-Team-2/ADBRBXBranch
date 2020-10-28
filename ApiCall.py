import requests as rq
import json
import pygal
import Constants
import date
import lxml

#API Query paramters
data = {
    "function":Constants.TIME_SERIES,
    "symbol":Constants.SYMBOL,
    "outputsize":"full",
    "interval":"60min",
    "apikey":Constants.API_KEY
    }

#Sending our request to the API using the information we put in the data collection.
apiCall = rq.get(Constants.API_URL, params=data)

#Stores the json-enconded content in the retrieved data.
response = apiCall.json()

# If statements to change key depending on the Time Serires selected. 
if Constants.TIME_SERIES == "TIME_SERIES_DAILY":
    timeSeries = "Time Series (Daily)"
elif Constants.TIME_SERIES == "TIME_SERIES_WEEKLY":
    timeSeries = "Weekly Time Series"
elif Constants.TIME_SERIES == "TIME_SERIES_MONTHLY":
    timeSeries = "Monthly Time Series"
    
    
#Retriving the dates in putting them into a dictonary.
dates = []
[dates.append(date) for date in response[timeSeries]]

#Making a set out of date so we can find its intersections.
set_2 = frozenset(date.date_strings)

#Reordering list to original sequence, finds intersection with oringal dates and the dates inbetween user input.
final_dates = [x for x in dates if x in set_2]

#Reverses the list because the list is put in reverse order.
final_dates.reverse()

#Creating a tuple of the dates so we can use them as key.
key = tuple(final_dates)

#Populating lists with data from API
opens = []
for x in range(len(key)):
    opens.append(response[timeSeries][key[x]]["1. open"])
    
highs = []
for x in range(len(key)):
    highs.append(response[timeSeries][key[x]]["2. high"])
    
lows = []
for x in range(len(key)):
    lows.append(response[timeSeries][key[x]]["3. low"])
    
closes = []
for x in range(len(key)):
    closes.append(response[timeSeries][key[x]]["4. close"])
    
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
