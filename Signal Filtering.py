import numpy as np
import matplotlib.pyplot as plt

# Membuat sinyal acak
np.random.seed(0)
signal_length = 100
signal = np.random.randn(signal_length)

# Membuat filter kernel (misalnya, filter rata-rata)
kernel_size = 5
filter_kernel = np.ones(kernel_size) / kernel_size

# Melakukan operasi konvolusi untuk filtering
filtered_signal = np.convolve(signal, filter_kernel, mode='same')

# Plot sinyal asli dan hasil filtering
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(signal, label='Sinyal Asli')
plt.title('Sinyal Asli')
plt.subplot(2, 1, 2)
plt.plot(filtered_signal, label='Hasil Filtering')
plt.title('Hasil Filtering')
plt.tight_layout()
plt.show()
