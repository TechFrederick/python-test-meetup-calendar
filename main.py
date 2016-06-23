from icalendar import Calendar
import datetime
import pycurl, json
from StringIO import StringIO

def get_cal(url):
  buffer = StringIO()
  c = pycurl.Curl()
  c.setopt(c.URL, url.rstrip('\n'))
  c.setopt(c.WRITEDATA, buffer)
  c.perform()
  c.close()
  body = buffer.getvalue()
  return body

def main():
  with open('cals.txt') as f:
      content = f.readlines()

  calendars = []
  for i in content:
    data = {}
    events = []
    body = get_cal(i)
    gcal = Calendar.from_ical(body)
    for component in gcal.walk():
      if component.name == "VCALENDAR":
        data['calendar_name'] = component.get('X-WR-CALNAME')
      if component.name == "VEVENT":
        event = {}
        event['summary'] = component.get('summary')
        event['date'] = component.get('dtstart').dt.strftime('%Y-%m-%d %H:%M')
        event['url'] = component.get('url')
        events.append(event)
    data['events'] = events
    calendars.append(data)

  print(json.dumps(calendars))

if __name__ == "__main__":
  main()
