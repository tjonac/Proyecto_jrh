import numpy as np
import matplotlib.pyplot as plt

class EcMov:
    def __init__(self,D,d):
        vx = np.arange(-d,D,0.01)
        self.vx=vx
        self.ec1 = np.sqrt((D+d)**2-(2*vx-D+d)**2)*D*d/(D+d)
        self.ec2 = -np.sqrt((D+d)**2-(2*vx-D+d)**2)*D*d/(D+d)
#está en 10^8 metros
Earth = EcMov(1520.98232,1470.98290)
plt.plot(Earth.vx,Earth.ec1)
plt.plot(Earth.vx,Earth.ec2)
plt.plot(0,0, marker="o", color="Yellow")
plt.show()