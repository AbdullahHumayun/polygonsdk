class Sec:
    def __init__(self, data):
        self.cik = data['cik']
        self.entityName = data['entityName']
        self.facts = data['facts']