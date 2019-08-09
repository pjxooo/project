class Initiatorscontributions(object):
    def __init__(self):
        self.initiatorsAndContributionsId = None
        self.annualReportYear = None
        self.initiator = None
        self.capitalContribution = None
        self.contributionTime = None
        self.modeOfInvestment = None
        self.companyId = None
    def getInitiatorsAndContributionsId(self):
        return self.initiatorsAndContributionsId
    def setInitiatorsAndContributionsId(self, value):
        self.initiatorsAndContributionsId = value
    def getAnnualReportYear(self):
        return self.annualReportYear
    def setAnnualReportYear(self, value):
        self.annualReportYear = value
    def getInitiator(self):
        return self.initiator
    def setInitiator(self, value):
        self.initiator = value
    def getCapitalContribution(self):
        return self.capitalContribution
    def setCapitalContribution(self, value):
        self.capitalContribution = value
    def getContributionTime(self):
        return self.contributionTime
    def setContributionTime(self, value):
        self.contributionTime = value
    def getModeOfInvestment(self):
        return self.modeOfInvestment
    def setModeOfInvestment(self, value):
        self.modeOfInvestment = value
    def getCompanyId(self):
        return self.companyId
    def setCompanyId(self, value):
        self.companyId = value
    def __str__(self):
        return "initiatorsAndContributionsId: " + self.initiatorsAndContributionsId + \
               ",annualReportYear: " + self.annualReportYear + \
               ",initiator: " + self.initiator + \
               ",capitalContribution: " + self.capitalContribution + \
               ",contributionTime: " + self.contributionTime + \
               ",modeOfInvestment: " + self.modeOfInvestment + \
               ",companyId"+self.companyId