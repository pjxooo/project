class Investment(object):
    def __init__(self):
        self.investmentId = None
        self.investedEnterprise = None
        self.investedEnterpriseRepresentative = None
        self.establishmentDate = None
        self.investmentProportion = None
        self.subscribedAmount = None
        self.state = None
        self.companyId = None
    def getInvestmentId(self):
        return self.investmentId
    def setInvestmentId(self,value):
        self.investmentId = value
    def getInvestedEnterprise(self):
        return self.investedEnterprise
    def setInvestedEnterprise(self, value):
        self.investedEnterprise = value
    def getInvestedEnterpriseRepresentative(self):
        return self.investedEnterpriseRepresentative
    def setInvestedEnterpriseRepresentative(self, value):
        self.investedEnterpriseRepresentative = value
    def getEstablishmentDate(self):
        return self.establishmentDate
    def setEstablishmentDate(self, value):
        self.establishmentDate = value
    def getInvestmentProportion(self):
        return self.investmentProportion
    def setInvestmentProportion(self, value):
        self.investmentProportion = value
    def getSubscribedAmount(self):
        return self.subscribedAmount
    def setSubscribedAmount(self, value):
        self.subscribedAmount = value
    def getState(self):
        return self.state
    def setState(self, value):
        self.state = value
    def getCompanyId(self):
        return self.companyId
    def setCompanyId(self, value):
        self.companyId = value
    def __str__(self):
        return "investmentId: "+self.investmentId+ \
                ",investedEnterprise: " + self.investedEnterprise + \
                ",investedEnterpriseRepresentative: " + self.investedEnterpriseRepresentative + \
                ",establishmentDate: " + self.establishmentDate + \
                ",investmentProportion: " + self.investmentProportion + \
                ",subscribedAmount: " + self.subscribedAmount + \
                ",state: " + self.state + \
                ",companyId" + self.companyId