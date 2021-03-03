x = 1
print ('sin(%g)=%g' % (x, sin(x)))
# There is no "import math.sin" or a simialr command therefore the program does not know what sin is.

x = 1
from math import sin
print ('sin(%g)=%g' % (x, sin(x)))
#This is correct program.