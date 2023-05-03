import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
C = np.array([[7, 8, 9], [1, 2, 3], [1, 2, 3]])

result_1 = A.dot(C)
print("The result_1 is dot")
print(result_1)

result_2 = np.inner(A, C)
print("The result_2 is inner")
print(result_2)

result_3 = np.outer(A, C)
print("The result_3 is outer")
print(result_3)

print("######################")

d = np.arange(0.1, 8, 1.2, float)
print(d)

a = np.linspace(0, 10, num = 5)
b = np.logspace(0, 10, num = 5)

print(a)
print(b)

G = [10**0, 10**2.5, 10**5, 10**7, 10**10]
print(G)