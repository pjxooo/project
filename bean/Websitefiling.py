class Websitefiling(object):
    def __init__(self):
        self.websiteFilingId = None
        self.homePage = None
        self.websiteName = None
        self.domainName = None
        self.recordNum = None
        self.companyId = None
    def getWebsiteFilingId(self):
        return self.websiteFilingId
    def setWebsiteFilingId(self, value):
        self.websiteFilingId = value
    def getHomePage(self):
        return self.homePage
    def setHomePage(self, value):
        self.homePage = value
    def getWebsiteName(self):
        return self.websiteName
    def setWebsiteName(self, value):
        self.websiteName = value
    def getDomainName(self):
        return self.domainName
    def setDomainName(self, value):
        self.domainName = value
    def getRecordNum(self):
        return self.recordNum
    def setRecordNum(self, value):
        self.recordNum = value
    def getCompanyId(self):
        return self.companyId
    def setCompanyId(self, value):
        self.companyId = value
    def __str__(self):
        return ",websiteFilingId: " + self.websiteFilingId +\
               ",homePage: " + self.homePage + \
               ",websiteName: " + self.websiteName + \
               ",domainName: " + self.domainName + \
               ",recordNum: " + self.recordNum + \
               ",companyId"+self.companyId