class Qualitysupervisi(object):
    def __init__(self):
        self.qualitySupervisiId = None
        self.sampleYear = None
        self.qualitySupervisiIdBatches = None
        self.qualitySupervisiProducts = None
        self.samplingResults = None
        self.companyId = None
    def getQualitySupervisiId(self):
        return self.qualitySupervisiId
    def setQualitySupervisiId(self, value):
        self.qualitySupervisiId = value
    def getSampleYear(self):
        return self.sampleYear
    def setSampleYear(self, value):
        self.sampleYear = value
    def getQualitySupervisiIdBatches(self):
        return self.qualitySupervisiIdBatches
    def setQualitySupervisiIdBatches(self, value):
        self.qualitySupervisiIdBatches = value
    def getQualitySupervisiProducts(self):
        return self.qualitySupervisiProducts
    def setQualitySupervisiProducts(self, value):
        self.qualitySupervisiProducts = value
    def getSamplingResults(self):
        return self.samplingResults
    def setSamplingResults(self, value):
        self.samplingResults = value
    def getCompanyId(self):
        return self.companyId
    def setCompanyId(self, value):
        self.companyId = value
    def __str__(self):
        return "qualitySupervisiId: "+self.qualitySupervisiId +\
               ",sampleYear: "+self.sampleYear +\
               ",qualitySupervisiIdBatches: "+self.qualitySupervisiIdBatches +\
               ",qualitySupervisiProducts: "+self.qualitySupervisiProducts +\
               ",samplingResults: "+self.samplingResults + \
               ",companyId: "+self.companyId