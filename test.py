from icalendar import Calendar
from datetime import datetime
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
        #print '-------------------'
        #print component.get('X-WR-CALNAME')
        data['calendar_name'] = component.get('X-WR-CALNAME')
        #print '-------------------'
      if component.name == "VEVENT":
        event = {}
        #print 'Summary: ' + component.get('summary')
        event['summary'] = component.get('summary')

        #print 'Date: ' + str(datetime.date(component.get('dtstart').dt))
        event['date'] = str(datetime.date(component.get('dtstart').dt))

        #print 'URL: ' + component.get('url')
        event['url'] = component.get('url')

        #print '-------------------'
        events.append(event)
    data['events'] = events
    calendars.append(data)

  print(json.dumps(calendars))

if __name__ == "__main__":
  main()
