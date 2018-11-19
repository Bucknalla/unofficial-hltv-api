from hltv import hltv
import pprint


h = hltv.match("2329057")

i = hltv.hltv()

pprint.pprint(i.upcomingMatches())



# for odd in h.odds():
#     print(type(odd[0]))
#     # print(odd[0])
#     if str(odd[0]) == 'betway':
#         print('adassda')

# print(h.maps())