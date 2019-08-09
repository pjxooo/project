class Abnormaloperation(object):
    def __init__(self):
        self.abnormalOperationId = None
        self.inTime = None
        self.inReason = None
        self.inOrganization = None
        self.outOfDate = None
        self.outReason = None
        self.outOrganization=None
        self.companyId=None
    def getAbnormalOperationId(self):
        return self.abnormalOperationId
    def setAbnormalOperationId(self, value):
        self.abnormalOperationId = value
    def getInTime(self):
        return self.inTime
    def setInTime(self, value):
        self.inTime = value
    def getInReason(self):
        return self.inReason
    def setInReason(self, value):
        self.inReason = value
    def getInOrganization(self):
        return self.inOrganization
    def setInOrganization(self, value):
        self.inOrganization = value
    def getOutOfDate(self):
        return self.outOfDate
    def setOutOfDate(self, value):
        self.outOfDate = value
    def getOutReason(self):
        return self.outReason
    def setOutReason(self, value):
        self.outReason = value
    def getOutOrganization(self):
        return self.outOrganization
    def setOutOrganization(self, value):
        self.outOrganization = value
    def getCompanyId(self):
        return self.companyId
    def setCompanyId(self, value):
        self.companyId = value
    def __str__(self):
        return "abnormalOperationId: "+self.abnormalOperationId +\
               ",inTime: "+self.inTime +\
               ",inReason: "+self.inReason + \
               ",inOrganization: " + self.inOrganization + \
               ",outOfDate: "+self.outOfDate +\
               ",outReason: "+self.outReason + \
               ",outOrganization: " + self.outOrganization + \
               ",companyId: "+self.companyId