class Changerecord(object):
    def __init__(self):
        self.changeRecordId = None
        self.changeRecordDate = None
        self.changedItem = None
        self.beforeChange = None
        self.afterChange = None
        self.companyId = None
    def getChangeRecordId(self):
        return self.changeRecordId
    def setChangeRecordId(self,value):
        self.changeRecordId = value
    def getchangeRecordDate(self):
        return self.changeRecordDate
    def setchangeRecordDate(self, value):
        self.changeRecordDate = value
    def getchangedItem(self):
        return self.changedItem
    def setchangedItem(self, value):
        self.changedItem = value
    def getbeforeChange(self):
        return self.beforeChange
    def setbeforeChange(self, value):
        self.beforeChange = value
    def getafterChange(self):
        return self.afterChange
    def setafterChange(self, value):
        self.afterChange = value
    def getCompanyId(self):
        return self.companyId
    def setCompanyId(self, value):
        self.companyId = value
    def __str__(self):
        return "changeRecordId: "+self.changeRecordId+ \
                ",changeRecordDate: " + self.changeRecordDate + \
                ",changedItem: " + self.changedItem + \
                ",beforeChange: " + self.beforeChange + \
                ",afterChange: " + self.afterChange + \
                ",companyId" + self.companyId