from func_PropriedadesMateriais import *
import numpy as np
import math



c30 = Concreto()
c45 = Concreto(45, 7, 1.4, 1.0)
conc = 40
c40 = Concreto(fck = conc)
'''
c35 = Concreto(35, alfa_e = 0.8)

c40 = Concreto(40, alfa_e = 0.8)

c45 = Concreto(45, alfa_e = 0.8)

c50 = Concreto(50, alfa_e = 0.8)


s01 = Aco(50, 8)

#print(vars(c01))
print('fck__ Ecs ______________ Eci')
print(c30.fck, c30.Ecs(), c30.Eci())
print(c35.fck, c35.Ecs(), c35.Eci())
print(c40.fck, c40.Ecs(), c40.Eci())
print(c45.fck, c45.Ecs(), c45.Eci())
print(c50.fck, c50.Ecs(), c50.Eci())

print(s01.gancho90())'''

print(c30.fck)