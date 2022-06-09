#import  modules to access specific fucntion  and classes
import random as rnd
#import pecific fucntion  or  classes exmaples
from random import randint
#all ffucntion  or  classes ein the module
from random import *

#python has number of modules that you can import
#You can also creat your own module and
#eg import the sumvalues fucntion  for the function files

import functions_variables as fnv

rand1 = rnd.randint(0,10)
rand2 = randint(0,10)
findareas = fnv.tri_area(rand1,rand2)

print(rand1,rand2)
print(findareas)
