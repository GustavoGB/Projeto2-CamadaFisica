import numpy as np
from matplotlib import animation 
import sounddevice as sd
import matplotlib.pyplot as plt
import soundfile as sf
import time as tm



fs = 44100
duration = 1


figura = plt.figure()
eixoX1 = figura.add_subplot(1,1,1)
plt.xlabel('Tempo')
plt.ylabel('Onda')
plt.axis = ([0,1000,-1000,1000])

sd.default.samplerate = fs
sd.default.channels = 1
arquivo_audio = "./audio/recebido"

def generateFilePath(fileName, counter):
    return fileName + str(counter) + ".wav"

def record_to_file(file, data, fs):
    sf.write(file, data, fs)

def soundDecoder(i):
    time=1
    tempo=np.linspace(0, time, fs*time)
    audio = sd.rec(int(duration*fs), fs, channels=1)
    sd.wait()

    y = audio[:,0]
    record_to_file(generateFilePath(arquivo_audio, 1), y, fs)
    eixoX1.clear()
    plt.xlim(0.01,0.02)
    eixoX1.plot(tempo[0:1000000], y[0:1000000])
    


decoder = animation.FuncAnimation(figura, soundDecoder, interval=1000)
    


plt.show()




