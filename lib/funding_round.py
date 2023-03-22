class FundingRound:

    FUNDING_ROUND_EXAMPLES = ["Angel", "Pre-Seed", "Seed", "Series A", "Series B", "Series C"]
    all = []


    def __init__(self, startup, Venture_Capitalist, type, investment):
        self._startup = startup
        self._venture_capitalist = Venture_Capitalist
        self.type = type
        self.investment = investment
        FundingRound.all.append(self)

    @property
    def startup(self):
        return self._startup
    
    @property
    def venture_capitalist(self):
        return self._venture_capitalist
    
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if type in FundingRound.FUNDING_ROUND_EXAMPLES:
            self._type = type

    def get_investment(self):
        return self._investment
    
    def set_investment(self, investment):
        if investment >= 0:
            self._investment = float(investment)

    investment = property(get_investment, set_investment)
