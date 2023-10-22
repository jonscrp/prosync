import json
import formatData

def createEvent(data):
    event = {
            'summary': formatData.summary(data),
            'location': '800 Howard St., San Francisco, CA 94103',
            'description': formatData.description(data),
            'start': {
            'dateTime': formatData.getFormatedDateTime(formatData.startDate(data)),
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': formatData.getFormatedDateTime(formatData.endDate(data)),
            'timeZone': 'America/Los_Angeles',
        },
        'recurrence': [
            'RRULE:FREQ=DAILY;COUNT=2'
        ],
        'attendees': [
            {'email': 'lpage@example.com'},
            {'email': 'sbrin@example.com'},
        ],
        'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }
    return event


