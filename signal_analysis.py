# oet24 amc272
# Oximeter Program
#%%
from numpy import fft
import numpy as np
import matplotlib.pyplot as plt

class Signal:
    def __init__(self):
        self.signal = []
        self.AddSignal()      
        self.readings = len(self.signal)
        self.duration = self.signal[self.readings-1][0]
        self.dt = self.duration/self.readings
        self.sampleFreq = 1/self.dt
        self.fundamentalFreq = self.sampleFreq/self.readings
        self.RemoveDCDrift()
        #self.ogSignal =
        self.spectrum = []
        #self.ogSpectrum = 

    def RemoveDCDrift(self):
        sum = 0
        for i in self.GetSignal():
            sum += i
        mean = sum/self.GetReadings()
        newSignal = []
        for i in self.GetSignal():
            newSignal.append(i - mean)
        self.SetSignal(newSignal)
                
    def AddSignal(self):
        with open("signal.txt", "r") as f:
            content = f.readlines()
        for line in content:
            if line.strip(): 
                parts = line.strip().split("\t")
                if len(parts) == 2:
                    time = float(parts[0])
                    value = float(parts[1])
                    self.signal.append([time, value])
        f.close()      

    def GetSignal(self):
        signalValues = []
        for reading in self.signal:
            signalValues.append(reading[1])
        return signalValues

    def GetTimes(self):
        timeValues = []
        for reading in self.signal:
            timeValues.append(reading[0])
        return timeValues
    
    def GetReadings(self):
        return self.readings
    
    def GetSampleFreq(self):
        return self.sampleFreq

    def SetSignal(self, newSignal):
        for reading in range(self.readings-1):
            self.signal[reading][1] = newSignal[reading]
       

    def SetSpectrum(self, spectrum):
        self.spectrum = spectrum

    def GetSpectrum(self):
        return self.spectrum


class SignalProcessor:
    def __init__(self, movAvgFactor, upperCutoff, lowerCutoff):
        self.movAvgFactor = movAvgFactor
        self.upperCutoff = upperCutoff
        self.lowerCutoff = lowerCutoff

    def MovingAverage(self, signal, length):
        pass
        
    def BandPass(self, signal,readings,fs):
        pass

    def FFT(self, signal, fs, readings):
        pass
    
    def IFFT(self, signal, fft_result, readings):
        pass


class SignalAnalysis:
    def __init__(self, filter, signal):
        self.filter = filter
        self.signal = signal
        self.CalculateSpectrum()
        self.output = SignalResult()

    def CleanSignal(self):
        pass

    def FilterSignal(self):
        pass

    def CalculateSpectrum(self):
        pass

    def Plot(self):  
        plt.plot(self.signal.GetSignal(), self.signal.GetTimes())

    def GetBPM(self):
        
        pass


class SignalResult:
    def __init__(self):
        pass

    def PlotSpectrum(self, spectrum):
        pass

    def PlotSignal(self, time, signal):
        pass

    def OutputSignalInfo(self):
        pass

    def OutputBPM(self):
        pass


Filter = SignalProcessor(50, 3.5, 0.5)
signal = Signal()
Analysis = SignalAnalysis(Filter, signal)

Analysis.Plot()
