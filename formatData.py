from datetime import datetime, timedelta, timezone

#import json
#schedule = json.load(open('reponse.json', 'r'))
#schedule = schedule['schedule']

# today date time 
# current_date = datetime.date.today()
def startDate(schedule):
    d = schedule['schedule'][0]['startDate'].split('/')
    month  = d[0]
    day  = d[1]
    year = d[2]

    time = schedule['schedule'][0]['startTime'].split()
    time_hour = time[0].split(':')
    hour = time_hour[0]
    min = time_hour[1]
    # am_pm= time[1]

    # Create a datetimeobject
    sd = datetime(int(year), int(month), int(day), int(hour), int(min), 0, 0)
    return sd



def endDate(schedule):
    d = schedule['schedule'][0]['endDate'].split('/')
    month  = d[0]
    day  = d[1]
    year = d[2]

    time = schedule['schedule'][0]['endTime'].split()
    time_hour = time[0].split(':')
    hour = time_hour[0]
    min = time_hour[1]
    # am_pm= time[1]

    # Create a datetimeobject
    ed = datetime(int(year), int(month), int(day), int(hour), int(min), 0, 0)
    return ed


def getFormatedDateTime(sd):
    # Define the time zone offset as -07:00 hours (Mountain Standard Time)
    tz_offset = timezone(timedelta(hours=-7))

    # Apply the time zone offset to the datetime object
    dt_with_offset = sd.replace(tzinfo=tz_offset)

    # Format the datetime object in ISO 8601 format
    formatted_Startdatetime = dt_with_offset.isoformat()
    return formatted_Startdatetime



def summary(schedule):
    s = schedule['schedule'][0]['ActivityName']
    return s

def description(schedule):
    d = schedule['schedule'][0]['Recommendations']
    return d

