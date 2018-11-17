from hltv import hltv
import pprint

# h = hltv.hltv()

for matches in hltv.hltv.upcomingMatches():
    pprint.pprint(matches)

h = hltv.match("2329057")

for odd in h.odds():
    print(type(odd[0]))
    # print(odd[0])
    if str(odd[0]) == 'betway':
        print('adassda')

print(h.maps())