 from math import pi
 import statistics
 from functools import reduce
 def area(r):
     return pi * r*r
 radii= [2,3,4,5,6]
 print(list(map(area,radii)))
 data=[2,3,4,6,7,8]
 avg = statistics.mean(data)
 print(list(filter(lambda x:x>avg,data)))
 given=[2,3,4,5,6]
 added=lambda x,y:x+y
 print(reduce(added,given))
 full_name=lambda fn,ln: fn.strip().title()+ ' ' +ln.strip().title()
 full=full_name('igata','john')
 print(full)
