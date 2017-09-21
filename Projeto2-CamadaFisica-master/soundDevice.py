import numpy as np
from matplotlib import animation 
import sounddevice as sd
import matplotlib.pyplot as plt



fs = 44100
duration = 1


figura = plt.figure()
eixoX1 = figura.add_subplot(1,1,1)
plt.xlabel('Tempo')
plt.ylabel('Onda')
plt.axis = ([0,1000,-1000,1000])



def soundDecoder(i):
    time=1
    tempo=np.linspace(0, time, fs*time)
    x = tempo

    audio = sd.rec(int(duration*fs), fs, channels=1)
    sd.wait()

    y = audio[:,0]

    eixoX1.clear()
    plt.xlim(0,0.015)
    eixoX1.plot(x[0:1000], y[0:1000])
    


decoder = animation.FuncAnimation(figura, soundDecoder, interval=1000)
    


plt.show()




