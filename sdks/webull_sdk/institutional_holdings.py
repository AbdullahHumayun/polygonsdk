class InstitutionHolding:
    def __init__(self, data):
        self.institution_holding = InstitutionStat(data['institutionHolding'])

class InstitutionStat:
    def __init__(self, data):
        self.stat = Stat(data['stat'])
        self.new_position = Position(data['newPosition'])
        self.increase = Position(data['increase'])
        self.sold_out = Position(data['soldOut'])
        self.decrease = Position(data['decrease'])

class Stat:
    def __init__(self, data):
        self.holding_count = data.get('holdingCount', None)
        self.holding_count_change = data.get('holdingCountChange', None)
        self.holding_ratio = data.get('holdingRatio', None)
        self.holding_ratio_change = data.get('holdingRatioChange', None)
        self.institutional_count = data.get('institutionalCount', None)

class Position:
    def __init__(self, data):
        self.holding_count_change = data.get('holdingCountChange', None)
        self.institutional_count = data.get('institutionalCount', None)