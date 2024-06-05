import numpy as np

generator_matrix = np.array([[1., 0., 0., 0., 0., 0.],
                             [0., 1., 0., 0., 0., 0.],
                             [0., 0., 1., 0., 0., 0.],
                             [0., 0., 0., 1., 0., 0.],
                             [0., 0., 0., 0., 1., 0.],
                             [0., 0., 0., 0., 0., 1.]])

message = np.array([1, 0, 1, 0, 1, 0])

codeword = np.dot(message, generator_matrix) % 2

print("Codeword:", codeword)
