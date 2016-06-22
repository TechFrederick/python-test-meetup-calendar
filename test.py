from icalendar import Calendar
from datetime import datetime
import pycurl
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

with open('cals.txt') as f:
    content = f.readlines()

for i in content:
    body = get_cal(i)
    gcal = Calendar.from_ical(body)
    for component in gcal.walk():
      if component.name == "VCALENDAR":
        print '-------------------'
        print component.get('X-WR-CALNAME')
        print '-------------------'
      if component.name == "VEVENT":
        print 'Summary: ' + component.get('summary')
        print 'Date: ' + str(datetime.date(component.get('dtstart').dt))
        print 'URL: ' + component.get('url')
        print '-------------------'
