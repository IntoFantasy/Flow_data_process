import numpy as np
import matplotlib.pyplot as plt
import pywt
import scipy
import cvxpy as cp
import warnings
warnings.filterwarnings("ignore")

data = np.loadtxt("output.txt")

sample_num = 500
model_num = 10
n = 3380

# 采样序列
sample_matrix = np.random.choice(range(3380), sample_num)
sample_matrix.sort()
# 采样
sample_data = data[sample_matrix].T
# 采样矩阵

print(sample_data.shape)
U, S, Vt = np.linalg.svd(sample_data)
# 重构
U_new = U[:, :model_num]
S_new = np.zeros((model_num, model_num))

for i in range(model_num):
    S_new[i][i] = S[i]
Vt_new = Vt[:model_num, :]
# print("Vt_new:\n", Vt_new)
# 压缩感知
Psi = np.linalg.inv(scipy.fft.dct(np.eye(n, n)))
Theta = Psi[sample_matrix]
Vt_re = np.zeros((model_num, n))
for i in range(model_num):
    x = cp.Variable(n)
    obj = cp.Minimize(cp.norm(x, 1))
    cons = [Theta @ x == Vt_new[i]]
    pro = cp.Problem(obj, cons)
    pro.solve()
    Vt_re[i] = scipy.ifft(x.value)
# 重构
Data_re = np.dot(np.dot(U_new, S_new), Vt_re).T
np.savetxt("re.txt", Data_re)
# print(Data_re.shape)
