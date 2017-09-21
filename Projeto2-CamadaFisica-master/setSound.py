import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np

fs = 44100
t=1

def som(list,num):
    f1 = list[0]
    f2 = list[1]


    om=(2 * np.pi *f1)
    om1=(2 * np.pi *f2)

    a = np.sin(tempo*om)
    b = np.sin(tempo*om1)

    y=a+b

    time=np.linspace(0, t, fs*t)
    plt.close("all")
    plt.plot(time, y)
    plt.xlim(0,0.015)
    plt.xlabel('tempo')
    plt.ylabel('onda')
    plt.show()

    sd.play(y, fs)
    sd.wait()