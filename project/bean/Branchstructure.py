class Branchstructure(object):
    def __init__(self):
        self.branchStructureId = None
        self.companyName = None
        self.leader = None
        self.establishmentDate = None
        self.state = None
        self.companyId = None
    def getBranchStructureId(self):
        return self.branchStructureId
    def setBranchStructureId(self,value):
        self.branchStructureId = value
    def getCompanyName(self):
        return self.companyName
    def setCompanyName(self, value):
        self.companyName = value
    def getLeader(self):
        return self.leader
    def setLeader(self, value):
        self.leader = value
    def getEstablishmentDate(self):
        return self.establishmentDate
    def setEstablishmentDate(self, value):
        self.establishmentDate = value
    def getState(self):
        return self.state
    def setState(self, value):
        self.state = value
    def getCompanyId(self):
        return self.companyId
    def setCompanyId(self, value):
        self.companyId = value
    def __str__(self):
        return "branchStructureId: "+self.branchStructureId+ \
                ",companyName: " + self.companyName + \
                ",leader: " + self.leader + \
                ",establishmentDate: " + self.establishmentDate + \
                ",state: " + self.state + \
                ",companyId" + self.companyId