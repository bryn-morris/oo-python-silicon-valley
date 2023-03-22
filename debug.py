from lib.funding_round import *
from lib.venture_capitalist import *
from lib.startup import *

# code here
# e.g.
#   s1 = Startup( 'Pied Piper', 'Richard Hendricks', 'www.pp.com' )
#   vc1 = VentureCapitalist( 'Peter Gregory', 100000000 )
#   fr1 = FundingRound( s1, vc1, 'Pre-Seed', 200000.99 )

s1 = Startup("testname", "testfounder", "testdomain")
s2 = Startup("DoggySitter", "Mick Swiggins", "www.dogsits.com")
s3 = Startup("ChickenSitter", "testfounder", "www.chickensits.com")

vc1 = VentureCapitalist("Bazoo", 10000000000)
vc2 = VentureCapitalist("Kevin", 5000)
vc3 = VentureCapitalist("Seth", 90000000)
vc4 = VentureCapitalist("Bezos", 212000000000)
vc5 = VentureCapitalist("Meat", 50)
vc6 = VentureCapitalist("Red Meat", 60000000000)

fr1 = FundingRound(s3,vc1,"Angel", 1500000000)
fr2 = FundingRound(s2,vc3,"Seed",300000)
fr3 = FundingRound(s3,vc5,"Angel", 17)
fr4 = FundingRound(s3,vc1,"Seed", 150000)
fr5 = FundingRound(s3, vc6,"Series B", 160000)

# do not remove
import ipdb; ipdb.set_trace()
