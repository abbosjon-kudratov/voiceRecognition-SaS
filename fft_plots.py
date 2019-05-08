
import matplotlib.pyplot as plt
#from scipy.fftpack import fft
#from myFFT import *
from customFFT import *
from scipy.io import wavfile   # get the api to read wav files
from scipy.signal import fftconvolve
import sys


fs_yes, yes = wavfile.read("yes.wav") # load the data
_yes = yes.T[0] # two channel soundtrack, we will get the first track
yes_fft = fft(_yes) # calculate fourier transform (complex numbers list)
yes_fft_len = len(yes_fft)//2  # we only need half of the fft list (real signal symmetry)


fs_no, no = wavfile.read("no.wav") # load the data
_no = no.T[0] # two channel soundtrack, we will get the first track
no_fft = fft(_no) # calculate fourier transform (complex numbers list)
no_fft_len = len(no_fft)//2  # we only need half of the fft list (real signal symmetry)


filename=sys.argv[1]

#fs_input, input_data = wavfile.read("test_no_2.wav") # load the data
fs_input, input_data = wavfile.read(filename) # load the data
_input = input_data.T[0] # two channel soundtrack, we will get the first track
input_fft = fft(_input) # calculate fourier transform (complex numbers list)
input_fft_len = len(input_fft)//2  # we only need half of the fft list (real signal symmetry)


convolve_yes=fftconvolve(_input, _yes, mode='same')
# mode='same' is for getting the maximum like the first argument to equalize the outputs
cy=convolve_yes*np.conj(convolve_yes)

convolve_no=fftconvolve(_input, _no, mode='same')
cn=convolve_no*np.conj(convolve_no)

convolve_yes_yes=fftconvolve(_yes, _yes, mode='same')
cyy=convolve_yes_yes*np.conj(convolve_yes_yes)

convolve_no_no=fftconvolve(_no, _no, mode='same')
cnn=convolve_no_no*np.conj(convolve_no_no)

#diff_yes=convolve_yes-convolve_yes_yes
#diff_no=convolve_no-convolve_no_no

'''
fig3=plt.figure()
fig3.add_subplot(711)
plt.plot(//data)
plt.title("Title")
'''

fig2=plt.figure()

fig2.add_subplot(311)
#plt.plot(convolve_yes)
plt.plot(cy)
plt.title('convolve with yes')

fig2.add_subplot(313)
#plt.plot(convolve_no)
plt.plot(cn)
plt.title('convolve with no')

'''
print(convolve_yes)
print("convolve no")
print(convolve_no)

mean_yes=np.mean(convolve_yes)
mean_no=np.mean(convolve_no)
mean_yes_yes=np.mean(convolve_yes_yes)
mean_no_no=np.mean(convolve_no_no)

mean_cy=np.mean(cy)
mean_cyy=np.mean(cyy)
mean_cn=np.mean(cn)
mean_cnn=np.mean(cnn)

print(mean_yes)
print(mean_no)
print(mean_yes_yes)
print(mean_no_no)

print(mean_cy)
print(mean_cyy)
print(mean_cn)
print(mean_cnn)	
'''

if((abs(abs(max(cy))-abs(max(cyy))) < abs(abs(max(cn))-abs(max(cnn)))) and max(cy)>max(cn)):
	print("Probably answer is YES")
else:
	print("Probably answer is NO")

if(max(cy) > max(cn)):
	print("According to max points: YES")
else:
	print("According to max points: NO")


if((abs(abs(max(cy))-abs(max(cyy))) < abs(abs(max(cn))-abs(max(cnn))))):
	print("According to difference between max points: YES")
else:
	print("According to difference between max points: NO")


fig = plt.figure()

fig.add_subplot(511)
plt.plot(abs(yes_fft[:(yes_fft_len-1)]),'r')
plt.title('FFT (YES)')

fig.add_subplot(513)
plt.plot(abs(no_fft[:(no_fft_len-1)]),'r')
plt.title('FFT (NO)')

fig.add_subplot(515)
plt.plot(abs(input_fft[:(input_fft_len-1)]),'r')
plt.title('FFT (input)')

plt.show()
