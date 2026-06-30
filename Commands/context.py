class Context() :
    def __init__(self):
        self.lasttopic = None
        self.lastpreference = None

    def set_topic(self,topic):
        self.lasttopic = topic
    def get_topic(self):
        return self.lasttopic
    def set_preference(self,pref):
        self.lastpreference = pref
    def get_preference(self):
        return self.lastpreference
    
    def reset(self):
        self.lasttopic = None
        self.lastpreference = None