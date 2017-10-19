import wave
import struct
import math
import numpy as np
import soundfile as sf
import sounddevice as sd
from scipy import signal as sg
from scipy.fftpack import fft, ifft

import matplotlib
matplotlib.use("TkAgg")
matplotlib.rcParams['agg.path.chunksize'] = 1000
from matplotlib import pyplot as plt

from transmissor import Transmissor

    def Receptor(transmissor,fs,recordingDuration):
        
        transmissor = Transmissor()
        fs = 44100 # khz
        recordingDuration = 10 # segundos
    
    def record(audio):
        """Grava audio por tempo determinado no construtor e retorna o sinal """
        audio = sd.rec(int(recordingDuration * fs),fs,channels=1)
        sd.wait()
        y = audio[:,0]
        return y

    def main(audio):
        # Grava 10s de audio e plota o fourier
        audio = record()
        faudiox,faudioy = transmissor.getFFT(audio)
        # plt.plot(faudiox,faudioy)
        # plt.show()

        # Recria os carriers a partir do audio gravado
        C1x,C1y = transmissor.createCarrier(7000,audio)
        C2x,C2y = transmissor.createCarrier(14000,audio)

        # Multiplica o audio gravado pelos carriers para demodular 
        dAM1 = audio * C1y
        dAM2 = audio * C2y
        fdAM1x,fdAM1y = transmissor.getFFT(dam1)
        fdAM2x,fdAM2y = transmissor.getFFT(dam2)
        
        #Exibe o fourrier

        fig, (ax1,ax2) = plt.subplots(1,2,figsize=(15,5))
        ax1.plot(fdAM1x,fdAM1y)
        ax2.plot(fdAM2x,fdAM2y)
        plt.show()

        # Faz um filtro passa baixa e reproduz os sons recuperados
        transmissor.play(transmissor.LPF(dAM1,3000,self.fs))
        transmissor.play(transmissor.LPF(dAM2,3000,self.fs))

Receptor().main()