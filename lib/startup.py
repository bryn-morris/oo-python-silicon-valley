from lib.venture_capitalist import *
from lib.funding_round import *

class Startup:

    # refactor to add list of fundingrounds per instance to reference in methods

    all = []
    domains = []
    
    def __init__(self, startup_name, founder, domain):
        self.name = startup_name
        # Founder needs to not be able to change! -> Property is read only
        self._founder = founder
        # Domain needs to not be able to change! -> Property is read only
        self._domain = domain

        Startup.domains.append(self.domain)
        Startup.all.append(self)

    @property
    def founder(self):
        return self._founder
    
    @property
    def domain(self):
        return self._domain
    
    def pivot(self, domain_string, name_string):
        self.name = name_string
        self._domain = domain_string
    
    @classmethod
    def find_by_founder(cls, founder_string):

        #generator Expression
        return next(s_o for s_o in cls.all if s_o.founder == founder_string)
        
        # founder_list = []

        # for startupobj in cls.all:
        #     if startupobj.founder == founder_string:
        #         founder_list.append(startupobj)
                

        # return founder_list[0]
    
    def sign_contract(self, vc_o, invest_type, amount_invested):
        
        #new_funding_round is a bucket that could take any name
        # the variable name isn't stored in the object itself

        FundingRound(self, vc_o, invest_type, amount_invested)


    @property
    def num_funding_rounds(self):

        # list = []

        # for funding_round in FundingRound.all:
        #     if funding_round.startup == self:
        #         list.append(funding_round)

        # return len(list)

        num_fund = 0

        for funding_round in FundingRound.all:
            if funding_round.startup == self:
                num_fund += 1
        
        return num_fund

    @property
    def total_funds(self):

        num_total = 0

        for funding_round in FundingRound.all:
            if funding_round.startup == self:
                num_total += funding_round.investment

        return num_total
    
    @property
    def investors(self):

        return list({fr.venture_capitalist.name for fr in FundingRound.all if fr.startup == self })

    @property
    def big_investors(self):

        beeeeg_list = []

        for fr in FundingRound.all:
            if fr.startup == self and fr.venture_capitalist.total_worth > 100000000:
                beeeeg_list.append(fr.type)

        return beeeeg_list
    
        # beeeeg_list = []

        # for fr in FundingRound.all:
        #     if fr.startup == self and fr.venture_capitalist in VentureCapitalist.tres_commas_club:
        #         beeeeg_list.append(fr.type)

        # return beeeeg_list