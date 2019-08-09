class Softwarecopyright(object):
    def __init__(self):
        self.softwareCopyrightInfoId = None
        self.sofewareWorksName = None
        self.versionNum = None
        self.registrationDate = None
        self.companyId = None
    def getSoftwareCopyrightInfoId(self):
        return self.softwareCopyrightInfoId
    def setSoftwareCopyrightInfoId(self, value):
        self.softwareCopyrightInfoId = value
    def getSofewareWorksName(self):
        return self.sofewareWorksName
    def setSofewareWorksName(self, value):
        self.sofewareWorksName = value
    def getVersionNum(self):
        return self.versionNum
    def setVersionNum(self, value):
        self.versionNum = value
    def getRegistrationDate(self):
        return self.registrationDate
    def setRegistrationDate(self, value):
        self.registrationDate = value
    def getCompanyId(self):
        return self.companyId
    def setCompanyId(self, value):
        self.companyId = value
    def __str__(self):
        return "softwareCopyrightInfoId: " + self.softwareCopyrightInfoId +\
               ",sofewareWorksName: " + self.sofewareWorksName + \
               ",versionNum: " + self.versionNum + \
               ",registrationDate: " + self.registrationDate + \
               ",companyId"+self.companyId