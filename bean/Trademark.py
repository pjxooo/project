class Trademark(object):
    def __init__(self):
        self.trademarkId = None
        self.trademarkName = None
        self.registrationNumber = None
        self.trademarkType = None
        self.effectiveTime = None
        self.processStatus = None
        self.companyId = None
    def getTrademarkId(self):
        return self.trademarkId
    def setTrademarkId(self, value):
        self.trademarkId = value
    def getTrademarkName(self):
        return self.trademarkName
    def setTrademarkName(self, value):
        self.trademarkName = value
    def getRegistrationNumber(self):
        return self.registrationNumber
    def setRegistrationNumber(self, value):
        self.registrationNumber = value
    def getTrademarkType(self):
        return self.trademarkType
    def setTrademarkType(self, value):
        self.trademarkType = value
    def getEffectiveTime(self):
        return self.effectiveTime
    def setEffectiveTime(self, value):
        self.effectiveTime = value
    def getProcessStatus(self):
        return self.processStatus
    def setProcessStatus(self, value):
        self.processStatus = value
    def getCompanyId(self):
        return self.companyId
    def setCompanyId(self, value):
        self.companyId = value
    def __str__(self):
        return "trademarkId: " + self.trademarkId +\
               ",trademarkName: " + self.trademarkName + \
               ",registrationNumber: " + self.registrationNumber + \
               ",trademarkType: " + self.trademarkType + \
               ",effectiveTime: " + self.effectiveTime + \
               ",processStatus: " + self.processStatus + \
               ",companyId"+self.companyId