class Brand(object):
    def __init__(self):
        self.brandInfoId = None
        self.brandName = None
        self.origin = None
        self.createdYear = None
        self.companyId = None
    def getBrandInfoId(self):
        return self.brandInfoId
    def setBrandInfoId(self, value):
        self.brandInfoId = value
    def getBrandName(self):
        return self.brandName
    def setBrandName(self, value):
        self.brandName = value
    def getOrigin(self):
        return self.origin
    def setOrigin(self, value):
        self.origin = value
    def getCreatedYear(self):
        return self.createdYear
    def setCreatedYear(self, value):
        self.createdYear = value
    def getCompanyId(self):
        return self.companyId
    def setCompanyId(self, value):
        self.companyId = value
    def __str__(self):
        return "brandInfoId: " + self.brandInfoId +\
               ",brandName: " + self.brandName + \
               ",origin: " + self.origin + \
               ",createdYear: " + self.createdYear + \
               ",companyId"+self.companyId