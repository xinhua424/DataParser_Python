from sympy import *
from sympy import pprint, collect
from sympy.abc import z
 
Kp = Symbol('Kp');
wp = Symbol('wp');
wz = Symbol('wz');
Ts = Symbol('Ts');
Ks = Symbol('Ks');
 
s = 2/Ts*(z-1)/(z+1)
 
H = Kp/s*(s+wz)/(s+wp)

 
pprint(simplify(collect(expand(H),z)))
