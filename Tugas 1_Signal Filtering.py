# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 23:23:12 2023

@author: ASUS
"""

import numpy as np 
import matplotlib.pyplot as plt

print ("Nama: Ammar Muzhaffar")
print ("NRP: 5009201074")

def generate_random_signal(length=100, seed= None):
    if seed is not None:
        np.random.seed(seed)
    signal = np.random.randn(length)
    return signal
def create_filter_kernel(kernel_size=5):
    filter_kernel = np.ones(kernel_size)/kernel_size
    return filter_kernel
def apply_convolution(signal, kernel):
    filtered_signal = np.convolve(signal, kernel, mode='some')
    return filtered_signal
def plot_signals(signal, filtered_signal):
    plt.figure(figsize=(12,8))
    
    plt.subplot(3,1,1)
    plt.plot(signal, label='Actual Signal')
    plt.title('Actual Signal')
    
    plt.subplot(3, 1, 2)
    plt.plot(filtered_signal, label='Filtering Signal')
    plt.title('Filtering Signal')
    
    plt.subplot(3, 1, 3)
    plt.plot(np.abs(np.fft.fft(signal)), label='Spektrum Actual Signal', color='green')
    plt.plot(np.abs(np.fft.fft(filtered_signal)), label='Spektrum Filtering Signal', color='red')
    plt.title('Spektrum')
    
    plt.tight_layout()
    plt.legend()
    plt.show()

signal_length = 100
signal = generate_random_signal(length=signal_length, seed=0)
kernel_size = 5
filter_kernel = create_filter_kernel(kernel_size=kernel_size)
filtered_signal = apply_convolution(signal, filter_kernel)
plot_signals(signal, filtered_signal)