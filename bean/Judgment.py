class Judgment(object):
    def __init__(self):
        self.judgmentId = None
        self.caseDate = None
        self.caseName = None
        self.causeOfAction = None
        self.caseStatus = None
        self.caseNum = None
        self.companyId = None
    def getJudgmentId(self):
        return self.judgmentId
    def setJudgmentId(self, value):
        self.judgmentId = value
    def getCaseDate(self):
        return self.caseDate
    def setCaseDate(self, value):
        self.caseDate = value
    def getCaseName(self):
        return self.caseName
    def setCaseName(self, value):
        self.caseName = value
    def getCauseOfAction(self):
        return self.causeOfAction
    def setCauseOfAction(self, value):
        self.causeOfAction = value
    def getCaseStatus(self):
        return self.caseStatus
    def setCaseStatus(self, value):
        self.caseStatus = value
    def getCaseNum(self):
        return self.caseNum
    def setCaseNum(self, value):
        self.caseNum = value
    def getCompanyId(self):
        return self.companyId
    def setCompanyId(self, value):
        self.companyId = value
    def __str__(self):
        return "judgmentId: "+self.judgmentId +\
               ",caseDate: "+self.caseDate +\
               ",caseName: "+self.caseName +\
               ",causeOfAction: "+self.causeOfAction +\
               ",caseStatus: "+self.caseStatus +\
               ",caseNum: "+self.caseNum +\
               ",companyId: "+self.companyId