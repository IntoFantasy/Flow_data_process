import numpy as np
import matplotlib.pyplot as plt
import pywt

data = np.loadtxt("output.txt")
print(data.shape)
layer_one = np.flip(data[0].reshape(16, 51), axis=0)

coeffs = pywt.dwt2(layer_one, "haar")
cA, (cH, cV, cD) = coeffs
color = "gray"
plt.figure(figsize=(26, 10))
plt.subplot(221)
plt.imshow(cA, color)
plt.subplot(222)
plt.imshow(cH, color)
plt.subplot(223)
plt.imshow(cV, color)
plt.subplot(224)
plt.imshow(cD, color)
plt.show()

