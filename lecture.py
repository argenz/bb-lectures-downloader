class Lecture(object): 
    def __init__(self, courseId, begin_timestamp, end_timestamp): 
        self.courseId = courseId
        self.begin_timestamp = begin_timestamp
        self.end_timestamp = end_timestamp
    
    def as_dict(self): 
        return {'courseId': self.courseId, 'begin_timestamp': self.begin_timestamp, 'end_timestamp': self.end_timestamp}
    
    def get_courseId(self):
        return self.courseId
    
    def get_begintimestamp(self): 
        return self.begin_timestamp
    
    def get_endtimestamp(self):
        return self.end_timestamp
    

