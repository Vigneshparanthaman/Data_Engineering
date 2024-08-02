lucky_draws = set()
print(type(lucky_draws),lucky_draws)

lucky_draws_o= {12,43,78,98,56,4,8,4,4,4,4,4,4,4,4,4,4,4,4,4,4}
lucky_draws_s= {11,22,33,44,55,66,99}
lucky_draws_s.add(90000000)
lucky_draws_s.discard(11)
lucky_draws_s.add(888888888)

print ("onlin draws", lucky_draws_o)
print ("shop draws " , lucky_draws_s)

"""
for draw in lucky_draws_o:
    print(draw)
"""
print(lucky_draws_s)
print(lucky_draws_o)
print("Union", lucky_draws_s|lucky_draws_o)

print("intersect", lucky_draws_s & lucky_draws_o)
print("different from the shop", lucky_draws_s - lucky_draws_o)
print("different from the online", lucky_draws_o - lucky_draws_s)

set1= {1,3,5}
set2= {3,1,5}
print (set1==set2)

S1=set1.clear()
print(S1)
print(set1)

print (set1==set2)





















