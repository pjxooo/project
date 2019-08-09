class Administrativepunishment(object):
    def __init__(self):
        self.administrativePunishmentId = None
        self.determineInstrumentNumber = None
        self.administrativePunishmentType = None
        self.decisiveOrganization = None
        self.decisiveDate = None
        self.companyId = None
    def getAdministrativePunishmentId(self):
        return self.administrativePunishmentId
    def setAdministrativePunishmentId(self, value):
        self.administrativePunishmentId = value
    def getDetermineInstrumentNumber(self):
        return self.determineInstrumentNumber
    def setDetermineInstrumentNumber(self, value):
        self.determineInstrumentNumber = value
    def getAdministrativePunishmentType(self):
        return self.administrativePunishmentType
    def setAdministrativePunishmentType(self, value):
        self.administrativePunishmentType = value
    def getDecisiveOrganization(self):
        return self.decisiveOrganization
    def setDecisiveOrganization(self, value):
        self.decisiveOrganization = value
    def getDecisiveDate(self):
        return self.decisiveDate
    def setDecisiveDate(self, value):
        self.decisiveDate = value
    def getCompanyId(self):
        return self.companyId
    def setCompanyId(self, value):
        self.companyId = value
    def __str__(self):
        return "administrativePunishmentId: "+self.administrativePunishmentId +\
               ",determineInstrumentNumber: "+self.determineInstrumentNumber +\
               ",administrativePunishmentType: "+self.administrativePunishmentType +\
               ",decisiveOrganization: "+self.decisiveOrganization +\
               ",decisiveDate: "+self.decisiveDate +\
               ",companyId: "+self.companyId