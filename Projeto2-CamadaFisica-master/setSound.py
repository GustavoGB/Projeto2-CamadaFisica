import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np

f1=666
f2=69420

fs = 44100
t=3
om=(2 * np.pi *f1)
om1=(2 * np.pi *f2)

a = np.sin(tempo*om)
b = np.sin(tempo*om1)

y=a+b

time=np.linspace(0, t, fs*t)
print (len(time), len(y))
plt.plot(time, y)
plt.xlim(0,0.015)
plt.xlabel('tempo')
plt.ylabel('onda')
plt.show()

sd.play(y, fs)
sd.wait()