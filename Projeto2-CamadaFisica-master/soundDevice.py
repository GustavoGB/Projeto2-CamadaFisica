import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np

fs = 44100
duration = 3

audio = sd.rec(int(duration*fs), fs, channels=1)
sd.wait()

y = audio[:,0]

time=np.linspace(0, t, fs*t)
print (len(time), len(y))
plt.plot(time, y)
plt.xlim(0,0.015)
plt.xlabel('tempo')
plt.ylabel('onda')
plt.show()
