# code to calculate area given radius as 0.43
# one can use from math  import pi 
import math
# 2.pi.r
C=2*math.pi*0.43
# pi.r^2
A=math.pi*0.43**2
# we are putting str c to concatenate the strings without str ,it will be float and strings which won't work
print("Circumference" +str(C))
print("Area" +str(A))