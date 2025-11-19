import numpy as np

def print_mat(mat):
    p = np.array2string(mat,separator=', ',)
    p = p.replace('[', '').replace(']', '')
    print(' ' + p)
    return

my_array = np.arange(10, 70, 2)
print(my_array)
print()

A = my_array.reshape(6, 5).transpose()
print_mat(A)
print()

A = (A * 2.5).astype(int)
A[1, :] = A[1, :] - 5
print_mat(A)
print()

B = np.random.uniform(0, 10, (6, 3))
print_mat(B)
print()

a = np.sum(A, axis=1)
b = np.sum(B, axis=0)
print(len(a), len(b))
print()

comp = A @ B
print_mat(comp)
print()

A = np.delete(A, 2, axis=1)
B = np.hstack((B, np.random.uniform(10, 20, (6, 3))))
print_mat(A)
print_mat(B)
print()

det_A = np.linalg.det(A)
det_B = np.linalg.det(B)
if det_A != 0:
    print_mat(np.linalg.inv(A))
else: print('Det A = 0')
if det_B != 0:
    print_mat(np.linalg.inv(B))
else: print('Det B = 0')
print()

A = np.linalg.matrix_power(A, 6)
B = np.linalg.matrix_power(B, -14)
print_mat(A)
print_mat(B)
print()

K_1 = np.array([[3, -1.2, -8, 8], [21, -19, 0.5, 0]])
G_1 = np.array([20, -8])
solution_1 = np.linalg.lstsq(K_1, G_1, rcond=None)[0]
print(solution_1)
print()

K_2 = np.array([[3, -1.2, -8, 8], [21, -19, 0.5, 0], [7, 0, -4.9, -2], [1, -2, 13, 9]])
G_2 = np.array([20, -8, 11, 3])
solution_2 = np.linalg.solve(K_2, G_2)
print(solution_2)



