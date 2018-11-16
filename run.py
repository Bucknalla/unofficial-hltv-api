from hltv import hltv

h = hltv.match("2329057")

# for odd in h.odds():
#     if("betway" in odd):
#         print(odd)
print(h.odds())