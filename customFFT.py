import cmath
# from math import log, ceil
import numpy as np

def pad(lst):
   '''padding the list to next nearest power of 2 as FFT implemented is radix 2'''
   k = 0
   while 2**k < len(lst):
      k += 1
   return np.concatenate((lst, ([0] * (2 ** k - len(lst)))))

def dft(data):
    """Compute the discrete Fourier Transform of the 1D array x"""
    data = np.asarray(data, dtype=float)
    N = data.shape[0]  #get the 1st dimension 
    # print(N)
    n = np.arange(N) 
    
    '''
    arange(N) function returns a array object containing 
    evenly spaced values within the given range.  
    It returns an evenly spaced values within a given interval.
    '''

    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, data)


def fft(data):
    """A recursive implementation of the 1D Cooley-Tukey FFT"""
    # fill zeroes
    data=pad(data)
    data = np.asarray(data, dtype=float)
    n = data.shape[0]  #get the 1st dimension   
    #print(n)
    if n <= 32:    # this cutoff should be optimized
        return dft(data)
    else:
        odd = fft(data[1::2])
        even = fft(data[::2])
        factor = np.exp(-2j * np.pi * np.arange(n) / n)
        return np.concatenate([even + factor[:n // 2] * odd,
                               even + factor[n // 2:] * odd])