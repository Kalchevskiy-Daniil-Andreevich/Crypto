import numpy as np

generator_matrix = np.array([[1., 0., 0., 0., 0., 0.],
                             [0., 1., 0., 0., 0., 0.],
                             [0., 0., 1., 0., 0., 0.],
                             [0., 0., 0., 1., 0., 0.],
                             [0., 0., 0., 0., 1., 0.],
                             [0., 0., 0., 0., 0., 1.]])

codeword = np.array([1, 0, 1, 0, 1, 0])


def introduce_errors(codeword, num_errors):
    error_positions = np.random.choice(
        len(codeword), num_errors, replace=False)

    noisy_codeword = np.copy(codeword)
    for pos in error_positions:
        noisy_codeword[pos] = 1 - noisy_codeword[pos]  # Flip the bit

    return noisy_codeword


for num_errors in range(3):
    noisy_codeword = introduce_errors(codeword, num_errors)
    print(f"Noisy Codeword with {num_errors} errors:", noisy_codeword)
