import urllib.request
import datetime as dt
import json

MAX_TIME_DIFFERENCE_MIN = 10

# function to open the JSON history file
def response(url):
    return urllib.request.urlopen(url)

# function to load the history data from the JSON
def loadJSON(response):
    return json.loads(response.read())

def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

def getAvgVelocity(data, route_id, current_time, weekday):
    totalVelocity = 0
    count = 0
    for i in data:
        # each entry in i is a data entry about a shuttle, loop through all of these.
        for j in i:
            # extract relevant data from this entry
            dataArrayTime = j["time"].split(":")
            dataHour = int(dataArrayTime[0].split("T")[1])
            dataMin = int(dataArrayTime[1])
            dataTime = dt.time(dataHour, dataMin, 0)

            dataArrayDay = dataArrayTime[0].split('-')
            dataYear = int(dataArrayDay[0])
            dataMonth = int(dataArrayDay[1])
            dataDay = int(dataArrayDay[2].split('T')[0])
            # get current weekday to prepare for ETA calculation
            day = dt.date(dataYear, dataMonth, dataDay)
            dataWeekday = day.weekday()

            # Only data from within 10 minutes of the current time should be considered in the ETA calculation.
            # Calculate start time (10 minutes before current time) and end time (10 minutes after current time).
w           start = dt.time(current_time.hour, current_time.minute, current_time.second)
            tmp_startDate = dt.datetime.combine(dt.date(1,1,1), start)
            
            start = tmp_startDate - dt.timedelta(minutes=MAX_TIME_DIFFERENCE_MIN)
            start = start.time()

            end = tmp_startDate + dt.timedelta(minutes=MAX_TIME_DIFFERENCE_MIN)
            end = end.time()

            # Determine whether the data we are looking at is within this range
            inTimeRange = time_in_range(start, end, dataTime)

            # The ETA calculation only cares about shuttles running on route_id on the current weekday and within
            # the time range. if this data entry fits these heuristics, consider it in the ETA calculation. If not, skip it.
            if j["route_id"] == route_id and dataWeekday == weekday and inTimeRange:
                # consider this data entry in the ETA algorithm
                totalVelocity += j["speed"]
                count += 1
            else:
                continue
    # perform final calculation for ETA algorithm and return result.
    return totalVelocity/count


if __name__ == '__main__':
    # Get what day of the week it is today
    targetWeekday = dt.datetime.today().weekday()
    targetWeekday = 2 # manually hard-coded the day we want
    # Get what the current time is now
    targetTime = dt.datetime.now().time()
    targetTime = dt.time(22, 45, 50) # manually hard-coded the time we want


    # Specify which route you want to calculate the average velocity for
    targetRoute = 20


    # URL of the JSON file that contains the history of the shuttles.
    url = "https://shuttles.rpi.edu/history"

    # open and load the JSON 
    response = response(url)
    data = loadJSON(response)
    
    # print(len(data))
    # for i in data:
    #     for j in i:
    #         print(j["time"].split(":"))
        # print(i)

    print(getAvgVelocity(data, 1, targetTime, targetWeekday))

