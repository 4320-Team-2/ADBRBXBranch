from datetime import date, timedelta, datetime
import Constants

start = datetime.strptime(Constants.START_DATE, "%Y-%m-%d")
end = datetime.strptime(Constants.END_DATE, "%Y-%m-%d")

sdate = start   # start date
edate = end   # end date

delta = edate - sdate       # as timedelta

stockDates = []

for i in range(delta.days + 1):
    day = sdate + timedelta(days=i)
    stockDates.append(day)

date_strings = []

for dt in stockDates:
    date_strings.append(dt.strftime("%Y-%m-%d"))
