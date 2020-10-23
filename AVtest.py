import requests as rq
import json
import pygal

#URL to Alphavantage API
API_URL = "https://www.alphavantage.co/query"

#Time Series Selection, ignore.
#print("Please Select a Time Series")
#print("1.) Intradaily")
#print("2.) Daily")
#print("3.) Weekly")
#print("4.) Monthly")
#seriesSelection = input("Please enter a selection (1, 2, 3, 4): ")

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

#Print tests to make sure the response is correct.
#print(response.keys())
#print(response.values())
#print(response)

#Test print that shows a pretty output of the json, it'll give you a good idea how the data structure looks.
#print(json.dumps(response, indent=4))

#Testing to see if the JSON file recived from the apiCall works by writing a local file.
#If you see how the data strcuture looks, the remove the "#" from the next three lines and run the code.
#f = open("test.txt","w")
#f.write(repr(response))
#f.close()

#Retriving the dates in putting them into a dictonary.
dates = []
[dates.append(date) for date in response["Time Series (Daily)"]]
#print(dates)

#I was delirous when I wrote this, I can't explain what I was doing here.
#key = tuple(dates)
#doubleDate = []
#for x in range(len(key)):
#	[doubleDate.append(day[key]) for day in dates]
#print(doubleDate)

#starts is a dictonary of the opening prices for the stock.
starts = []

#An implentation of trying to put the opening prices into the dict. I don't remeber what I was doing here either, ignore for now
#for date in response["Time Series (Daily)"]:
#	for opening in response["Time Series (Daily)"][date]["1. open"]:
#		[starts.append(opening)]


#Creating a tuple of the dates so we can use them as key.
key = tuple(dates)

#this is suppose to access the opening prices and put them into a dictonary
#the first loop basically assings the first date found
#the second loop then access the opening prices and appends them into the starts dictonary
#however this is where my problem starts. Instead of appending the whole price number, it instead splits it up individually
#for example, "110.155" is instead appended as "1" "1" "0" "." "1" "5" "5"
#i have no clue how to make it work as intended
for x in range(len(key)):
	for opening in response["Time Series (Daily)"][key[x]]["1. open"]:
		[starts.append(opening)]
print(starts)

#My really hacky solution that doesn't actually work at all, ignore for now.
#price = ""
#for x in range(len(key)):
#        for opening in response["Time Series (Daily)"][key[x]]["1. open"]:
#                price += opening
#tests = ' '.join(price[i:i + 8] for i in range(0, len(price), 8))

#put the dict infomartion into graphs and rendering them, not fully implemented so ignore for now. 
#bar_chart = pygal.Line()
#bar_chart.x_labels = dates
#bar_chart.render_to_file("populationviz.svg")
#print("Success!")
