import numpy as np
import matplotlib.pyplot as plt

pre = "Flow_dataset/Flow_dataset/sss-_"
back = ".dat"
data = []
# 选取一个位置，记录速度
target_position = 30
speed = []
for i in range(1, 6760, 2):
    Id = "{:0>6}".format(i)
    path = pre + Id + back
    num = 1
    vector = []
    with open(path) as f:
        for line in f:
            if 6 <= num < 822:
                line_data = line.split("\t")
                vector.append(float(line_data[6]))
            num += 1
    data.append(vector)
    speed.append(vector[target_position])

data_out = np.array(data)
speed_data = np.array(speed)
# np.savetxt("output.txt", data_out)
plt.plot(range(1, 6760, 2), speed_data)
plt.title("Speed Change")
plt.xlabel("time")
plt.ylabel("speed")
plt.show()
