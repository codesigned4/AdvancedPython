import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,10,100)

plt.subplot(2,1,1)
plt.plot(x,np.sin(x))
plt.xlabel("x ekseni")
plt.ylabel("y ekseni")
plt.legend(["sin"])


plt.subplot(2,1,2)
plt.plot(x,np.cos(x),color="r")
plt.xlabel("x ekseni")
plt.ylabel("y ekseni")
plt.legend(["cos"])

plt.tight_layout()

plt.savefig("sin-cos.png")

#plt.show()
