import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("re.txt")
print(data.shape)
for i in range(200):
    pic = data[i].reshape(16, 51)
    pic = np.flip(pic, axis=0)
    plt.imshow(pic, 'gray')
    plt.savefig("picture/DataRe-500-10/pic-{0}".format(i))


