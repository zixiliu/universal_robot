import numpy as np
from ur_kin_py.kin import Kinematics
kin = Kinematics('ur5') # or ur10
print kin.forward([0.0, -np.pi/2, np.pi/2, -np.pi/2, -np.pi/2, 0.0])
