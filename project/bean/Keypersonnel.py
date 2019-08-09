class Keypersonnel(object):
    def __init__(self):
        self.keyPersonnelID = None
        self.keyPersonnelName = None
        self.keyPersonnelDuty = None
        self.companyId = None
    def getKeyPersonnelID(self):
        return self.keyPersonnelID
    def setKeyPersonnelID(self, value):
        self.keyPersonnelID = value
    def getKeyPersonnelName(self):
        return self.keyPersonnelName
    def setKeyPersonnelName(self, value):
        self.keyPersonnelName = value
    def getKeyPersonnelDuty(self):
        return self.keyPersonnelDuty
    def setKeyPersonnelDuty(self, value):
        self.keyPersonnelDuty = value
    def getCompanyId(self):
        return self.companyId
    def setCompanyId(self, value):
        self.companyId = value
    def __str__(self):
        return ",keyPersonnelName: " + self.keyPersonnelName +\
               ",keyPersonnelDuty: " + self.keyPersonnelDuty + \
               ",companyId"+self.companyId