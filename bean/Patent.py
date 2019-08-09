class Patent(object):
    def __init__(self):
        self.patentId = None
        self.patentName = None
        self.applicationPublicationNum = None
        self.patentType = None
        self.publicationTime = None
        self.companyId = None
    def getPatentId(self):
        return self.patentId
    def setPatentId(self, value):
        self.patentId = value
    def getPatentName(self):
        return self.patentName
    def setPatentName(self, value):
        self.patentName = value
    def getApplicationPublicationNum(self):
        return self.applicationPublicationNum
    def setApplicationPublicationNum(self, value):
        self.applicationPublicationNum = value
    def getPatentType(self):
        return self.patentType
    def setPatentType(self, value):
        self.patentType = value
    def getPublicationTime(self):
        return self.publicationTime
    def setPublicationTime(self, value):
        self.publicationTime = value
    def getCompanyId(self):
        return self.companyId
    def setCompanyId(self, value):
        self.companyId = value
    def __str__(self):
        return "patentId: " + self.patentId +\
               ",patentName: " + self.patentName + \
               ",applicationPublicationNum: " + self.applicationPublicationNum + \
               ",patentType: " + self.patentType + \
               ",publicationTime: " + self.publicationTime + \
               ",companyId"+self.companyId