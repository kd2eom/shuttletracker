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
            start = dt.time(current_time.hour, current_time.minute, current_time.second)
            tmp_startDate = dt.datetime.combine(dt.date(1,1,1), start)
            
            start = tmp_startDate - dt.timedelta(minutes=MAX_TIME_DIFFERENCE_MIN)
            start = start.time()

            end = tmp_startDate + dt.timedelta(minutes=MAX_TIME_DIFFERENCE_MIN)
            end = end.time()

            # Determine whether the data we are looking at is within this range
            inTimeRange = time_in_range(start, end, dataTime)

            if j["route_id"] == route_id and dataWeekday == weekday and inTimeRange:
                totalVelocity += j["speed"]
                count += 1
            else:
                continue
    # perform final calculation for ETA algorithm and return result.
    return totalVelocity/count

def getAvgVelocity2(data, route_id, current_time, weekday):
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
            start = dt.time(current_time.hour, current_time.minute, current_time.second)
            tmp_startDate = dt.datetime.combine(dt.date(1,1,1), start)
            
            start = tmp_startDate - dt.timedelta(minutes=MAX_TIME_DIFFERENCE_MIN)
            start = start.time()

            end = tmp_startDate + dt.timedelta(minutes=MAX_TIME_DIFFERENCE_MIN)
            end = end.time()

            # Determine whether the data we are looking at is within this range
            inTimeRange = time_in_range(start, end, dataTime)

            if dataWeekday == weekday and inTimeRange:
                totalVelocity += j["speed"]
                count += 1
            else:
                continue
    # perform final calculation for ETA algorithm and return result.
    return totalVelocity/count

def getAvgVelocity3(data, route_id, current_time, weekday):
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
            start = dt.time(current_time.hour, current_time.minute, current_time.second)
            tmp_startDate = dt.datetime.combine(dt.date(1,1,1), start)
            
            start = tmp_startDate - dt.timedelta(minutes=15)
            start = start.time()

            end = tmp_startDate + dt.timedelta(minutes=15)
            end = end.time()

            # Determine whether the data we are looking at is within this range
            inTimeRange = time_in_range(start, end, dataTime)


            if j["route_id"] == route_id and dataWeekday == weekday and inTimeRange:
                totalVelocity += j["speed"]
                count += 1
            else:
                continue
    # perform final calculation for ETA algorithm and return result.
    return totalVelocity/count

def getAvgVelocity4(data, route_id, current_time, weekday):
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
            start = dt.time(current_time.hour, current_time.minute, current_time.second)
            tmp_startDate = dt.datetime.combine(dt.date(1,1,1), start)
            
            start = tmp_startDate - dt.timedelta(minutes=20)
            start = start.time()

            end = tmp_startDate + dt.timedelta(minutes=20)
            end = end.time()

            # Determine whether the data we are looking at is within this range
            inTimeRange = time_in_range(start, end, dataTime)


            if j["route_id"] == route_id and dataWeekday == weekday and inTimeRange:
                totalVelocity += j["speed"]
                count += 1
            else:
                continue
    # perform final calculation for ETA algorithm and return result.
    return totalVelocity/count

def getAvgVelocity5(data, route_id, current_time, weekday):
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
            start = dt.time(current_time.hour, current_time.minute, current_time.second)
            tmp_startDate = dt.datetime.combine(dt.date(1,1,1), start)
            
            start = tmp_startDate - dt.timedelta(minutes=30)
            start = start.time()

            end = tmp_startDate + dt.timedelta(minutes=30)
            end = end.time()

            # Determine whether the data we are looking at is within this range
            inTimeRange = time_in_range(start, end, dataTime)

            if j["route_id"] == route_id and dataWeekday == weekday and inTimeRange:
                totalVelocity += j["speed"]
                count += 1
            else:
                continue
    # perform final calculation for ETA algorithm and return result.
    return totalVelocity/count

def getAvgVelocity6(data, route_id, current_time, weekday):
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
            start = dt.time(current_time.hour, current_time.minute, current_time.second)
            tmp_startDate = dt.datetime.combine(dt.date(1,1,1), start)
            
            start = tmp_startDate - dt.timedelta(minutes=MAX_TIME_DIFFERENCE_MIN)
            start = start.time()

            end = tmp_startDate + dt.timedelta(minutes=MAX_TIME_DIFFERENCE_MIN)
            end = end.time()

            # Determine whether the data we are looking at is within this range
            inTimeRange = time_in_range(start, end, dataTime)


            if j["route_id"] == route_id and inTimeRange:
                totalVelocity += j["speed"]
                count += 1
            else:
                continue
    # perform final calculation for ETA algorithm and return result.
    return totalVelocity/count

def getAvgVelocity8(data, route_id, current_time, weekday, vehicle_id):
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
            start = dt.time(current_time.hour, current_time.minute, current_time.second)
            tmp_startDate = dt.datetime.combine(dt.date(1,1,1), start)
            
            start = tmp_startDate - dt.timedelta(minutes=MAX_TIME_DIFFERENCE_MIN)
            start = start.time()

            end = tmp_startDate + dt.timedelta(minutes=MAX_TIME_DIFFERENCE_MIN)
            end = end.time()

            # Determine whether the data we are looking at is within this range
            inTimeRange = time_in_range(start, end, dataTime)

            if j["route_id"] == route_id and dataWeekday == weekday and inTimeRange and j["vehicle_id"] == vehicle_id:
                totalVelocity += j["speed"]
                count += 1
            else:
                continue
    # perform final calculation for ETA algorithm and return result.
    return totalVelocity/count

if __name__ == '__main__':
    # Get what day of the week it is today
    targetWeekday = dt.datetime.today().weekday()
    targetWeekday = 2 # manually hard-code the day we want
    # Get what the current time is now
    targetTime = dt.datetime.now().time()
    targetTime = dt.time(22, 45, 50) # manually hard-coded the time we want


    # Specify which route you want to calculate the average velocity for
    targetRoute = 1
    # Specify the shutlte's vehicle_id number
    shuttleID = 9


    # URL of the JSON file that contains the history of the shuttles.
    url = "https://shuttles.rpi.edu/history"

    # open and load the JSON 
    response = response(url)
    data = loadJSON(response)
    
    # Run 7 different versions of the ETA algorithm (each version uses a different heuristic for calculation) and
    # output the results we get under each version.
    # Each version will use the exact same data; thus, any differences in output are solely due to differences
    # in the algorithm. 

    print("Version 1 (default): ")
    print(getAvgVelocity(data, 1, targetTime, targetWeekday))

    print("Version 2: Same as 1, but shuttle doesn't have to be on route_id (can be on any route).")
    print(getAvgVelocity2(data, 1, targetTime, targetWeekday))

    print("Version 3: Same as 1, but change time window to 15 minutes instead of 10.")
    print(getAvgVelocity3(data, 1, targetTime, targetWeekday))

    print("Version 4: Same as 1, but change time window to 20 minutes instead of 10")
    print(getAvgVelocity4(data, 1, targetTime, targetWeekday))

    print("Version 5: Same as 1, but change time window to 30 minutes instead of 10")
    print(getAvgVelocity5(data, 1, targetTime, targetWeekday))

    print("Version 6: Same as 1, but look at ANY DAY OF THE WEEK.")
    print(getAvgVelocity6(data, 1, targetTime, targetWeekday))

    print("Version 7: Same as 1, but shuttle must HAVE THE SAME SHUTTLE ID AS THE SHUTTLE WE ARE TARGETING.")
    print(getAvgVelocity8(data, 1, targetTime, targetWeekday, shuttleID))

    '''
    RESULTS (as of 2/16/19 at 4:08 PM):

Version 1 (default): 
12.233058956086635

Version 2: Same as 1, but shuttle doesn't have to be on route_id (can be on any route).
13.024325100523708

Version 3: Same as 1, but change time window to 15 minutes instead of 10.
11.852338474319906

Version 4: Same as 1, but change time window to 20 minutes instead of 10
12.49505608883642

Version 5: Same as 1, but change time window to 30 minutes instead of 10
12.113736460390298

Version 6: Same as 1, but look at ANY DAY OF THE WEEK.
12.554997379680035

Version 7: Same as 1, but shuttle must HAVE THE SAME SHUTTLE ID AS THE SHUTTLE WE ARE TARGETING.
12.183459281921387

    '''

