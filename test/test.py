import random
import math


rlist = ["string", 1.234, 238]

_ten_list = list(range(10))

for i in _ten_list:
    print("{}: {}".format(_ten_list.index(i), i))

print(rlist[0] * 3)

_dx = rlist.count("string")
_idx = rlist.index("string")

print("string" in rlist)
print("'{}' @ index: {}".format("string", _idx))
print("How amny times '{}' in rlist: {}".format("string", _dx))
