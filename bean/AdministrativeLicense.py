class AdministrativeLicense(object):
    def __init__(self):
        self.administrativeLicenseId = None
        self.administrativeLicenseNum = None
        self.licenseName = None
        self.licenseContent = None
        self.beginOfValidity = None
        self.stopOfValidity = None
        self.licensingAuthority = None
        self.companyId = None
    def getAdministrativeLicenseId(self):
        return self.administrativeLicenseId
    def setAdministrativeLicenseId(self, value):
        self.administrativeLicenseId = value
    def getAdministrativeLicenseNum(self):
        return self.administrativeLicenseNum
    def setAdministrativeLicenseNum(self, value):
        self.administrativeLicenseNum = value
    def getLicenseName(self):
        return self.licenseName
    def setLicenseName(self, value):
        self.licenseName = value
    def getLicenseContent(self):
        return self.licenseContent
    def setLicenseContent(self, value):
        self.licenseContent = value
    def getBeginOfValidity(self):
        return self.beginOfValidity
    def setBeginOfValidity(self, value):
        self.beginOfValidity = value
    def getStopOfValidity(self):
        return self.stopOfValidity
    def setStopOfValidity(self, value):
        self.stopOfValidity = value
    def getLicensingAuthority(self):
        return self.licensingAuthority
    def setLicensingAuthority(self, value):
        self.licensingAuthority = value
    def getCompanyId(self):
        return self.companyId
    def setCompanyId(self, value):
        self.companyId = value
    def __str__(self):
        return "administrativeLicenseId: "+self.administrativeLicenseId +\
               ",administrativeLicenseNum: "+self.administrativeLicenseNum +\
               ",licenseName: "+self.licenseName +\
               ",licenseContent: "+self.licenseContent +\
               ",beginOfValidity: "+self.beginOfValidity + \
               ",stopOfValidity: " + self.stopOfValidity + \
               ",licensingAuthority: " + self.licensingAuthority +\
               ",companyId: "+self.companyId