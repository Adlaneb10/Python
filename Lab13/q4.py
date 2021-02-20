d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = {}
d3['a'] = d1['a'] + d2['a']
d3['b'] = d1['b'] + d2['b']
d3['d'] = d2['d']
d3['c'] = d1['c']

print(d3)

#Better method for this program

#for key in d1:
#    d3[key] += d2[key]

#for key in d2:
#    if key in d1.keys():
#        d3[key] += d2[key]
#    else:
#        d3[key] = d2[key]

#print(d3)
