class Shareholder(object):
    def __init__(self):
        self.shareHolderId = None
        self.shareHolder = None
        self.shareholdingRatio = None
        self.subscribedCapitalContribution = None
        self.actualCapitalContribution = None
        self.companyId = None
    def getShareHolderId(self):
        return self.shareHolderId
    def setShareHolderId(self, value):
        self.shareHolderId = value
    def getShareHolder(self):
        return self.shareHolder
    def setShareHolder(self, value):
        self.shareHolder = value
    def getShareholdingRatio(self):
        return self.shareholdingRatio
    def setShareholdingRatio(self, value):
        self.shareholdingRatio = value
    def getSubscribedCapitalContribution(self):
        return self.subscribedCapitalContribution
    def setSubscribedCapitalContribution(self, value):
        self.subscribedCapitalContribution = value
    def getActualCapitalContribution(self):
        return self.actualCapitalContribution
    def setActualCapitalContribution(self, value):
        self.actualCapitalContribution = value
    def getCompanyId(self):
        return self.companyId
    def setCompanyId(self, value):
        self.companyId = value

    def __str__(self):
        return ",shareHolderId: " + self.shareHolderId +\
               ",shareHolder: " + self.shareHolder + \
                ",shareholdingRatio: " + self.shareholdingRatio +\
               ",subscribedCapitalContribution: " + self.subscribedCapitalContribution +\
               ",actualCapitalContribution: " + self.actualCapitalContribution +\
               ",companyId: "+self.companyId