from lib.funding_round import *
from lib.startup import *

class VentureCapitalist:
    
    all = []
    tres_commas_club = []
    FUNDING_ROUND_EXAMPLES = ["Angel", "Pre-Seed", "Seed", "Series A", "Series B", "Series C"]

    def __init__(self, vc_name, net_worth):
        self.name = vc_name
        self.total_worth = net_worth

        VentureCapitalist.all.append(self)

        if net_worth > 1000000000:
            VentureCapitalist.tres_commas_club.append(self)

    def offer_contract(self, startup_object, invest_type, amount_invested):

        new_founding_round = FundingRound(startup_object, self, invest_type, amount_invested )
        
    @property
    def funding_rounds(self):

        return [fr for fr in FundingRound.all if fr.venture_capitalist == self]

    @property
    def portfolio(self):

        return list({fr.startup for fr in self.funding_rounds})
    
    @property
    def biggest_investment(self):

        #still working on this!!!

        beeg_investment_list = [fr.investment for fr in self.funding_rounds]
        beeg_investment_list.sort(reverse=True)
        print(beeg_investment_list)

    