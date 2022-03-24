from datetime import datetime
from lecture import Lecture
import logging as log 
from ics import Calendar as iCal
import requests 

class myCalendar(object): 
    def __init__(self, ical_url):

        ical = iCal(requests.get(ical_url).text)
        events = list(ical.timeline)
        
        lectures_list = []
        for e in events: 
            tmp_lecture = Lecture(int(e.name[0:5]), e.begin.timestamp, e.end.timestamp)
            lectures_list.append(tmp_lecture)

        self.lectures = lectures_list
    
    def get_lectures_today(self): 
        end_time =  datetime.timestamp(datetime.now())
        begin_time = datetime.timestamp(datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)) #- 24*60*60 UNCOMMENT THIS FOR LECTURES OF TODAY AND YESTERDAY
        return list(filter(lambda lecture: (lecture.begin_timestamp > begin_time and lecture.begin_timestamp < end_time), self.lectures))
    
    def get_courseIds_today(self): 
        lectures = self.get_lectures_today()
        courseIds = list(set([lec.get_courseId() for lec in lectures]))
        return courseIds
