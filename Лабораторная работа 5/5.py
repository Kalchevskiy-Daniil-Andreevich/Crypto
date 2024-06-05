import numpy as np

# Generator Matrix
generator_matrix = np.array([[1., 0., 0., 0., 0., 0.],
                             [0., 1., 0., 0., 0., 0.],
                             [0., 0., 1., 0., 0., 0.],
                             [0., 0., 0., 1., 0., 0.],
                             [0., 0., 0., 0., 1., 0.],
                             [0., 0., 0., 0., 0., 1.]])

# Codeword
codeword = np.array([1, 0, 1, 0, 1, 0])  # Example codeword


def introduce_errors(codeword, num_errors):
    # Generate random positions for errors
    error_positions = np.random.choice(
        len(codeword), num_errors, replace=False)

    # Introduce errors
    noisy_codeword = np.copy(codeword)
    for pos in error_positions:
        noisy_codeword[pos] = 1 - noisy_codeword[pos]  # Flip the bit

    return noisy_codeword

# Function to compute syndrome


def compute_syndrome(codeword):
    return np.dot(codeword, generator_matrix.T) % 2

# Function to correct single error


def correct_single_error(codeword, syndrome):
    error_position = np.where(
        np.all(generator_matrix.T == syndrome, axis=1))[0][0]
    corrected_codeword = np.copy(codeword)
    corrected_codeword[error_position] = 1 - corrected_codeword[error_position]
    return corrected_codeword


# Test with different numbers of errors
for num_errors in range(3):
    noisy_codeword = introduce_errors(codeword, num_errors)
    print("Noisy Codeword with {} errors:".format(num_errors), noisy_codeword)
    syndrome = compute_syndrome(noisy_codeword)
    print("Syndrome:", syndrome)

    if np.any(syndrome):
        if np.sum(syndrome) == 1:  # Single error
            corrected_codeword = correct_single_error(noisy_codeword, syndrome)
            print("Corrected Codeword:", corrected_codeword)
        else:
            print("Cannot correct more than one error.")
    else:
        print("No errors detected.")
