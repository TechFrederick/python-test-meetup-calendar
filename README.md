## Python example: Meetup Calendar info

Install:
```sudo pip install -r requirements.txt```

Run:
```python test.py```

Output will look like:
```
$ python test.py | python -mjson.tool
[
    {
        "calendar_name": "Upcoming in Amazon Web Services - Frederick",
        "events": []
    },
    {
        "calendar_name": "Upcoming in Python Frederick",
        "events": [
            {
                "date": "2016-07-13",
                "summary": "2nd Wednesday Talk - AWS SDK (boto)",
                "url": "http://www.meetup.com/python-frederick/events/230370891/"
            }
        ]
    },
    {
        "calendar_name": "Upcoming in Frederick Linux Users Group (KeyLUG)",
        "events": [
            {
                "date": "2016-07-02",
                "summary": "Summer Coffee Chill Out",
                "url": "http://www.meetup.com/KeyLUG/events/229488165/"
            },
            {
                "date": "2016-08-06",
                "summary": "Shell Scripting\u2014Open Workshop",
                "url": "http://www.meetup.com/KeyLUG/events/231885756/"
            }
        ]
    },
    {
        "calendar_name": "Upcoming in Frederick Web Technology Group",
        "events": [
            {
                "date": "2016-07-05",
                "summary": "Presentation: Technology Meetup (Topic to be determined)",
                "url": "http://www.meetup.com/FredWebTech/events/230601373/"
            }
        ]
    }
]

