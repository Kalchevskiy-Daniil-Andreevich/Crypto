import numpy as np
from sympy import symbols, div


def generate_generator_matrix(n, k):
    x = symbols('x')
    G_X = x**k + 1
    generator_matrix = []

    for i in range(n - k + 1):
        row = []
        for j in range(n):
            if j < k:
                quotient, remainder = div(G_X, x**i, domain='GF(2)')
                if remainder.coeff(x**j) != 0:
                    row.append(1)
                else:
                    row.append(0)
            else:
                if j == i + k - 1:
                    row.append(1)
                else:
                    row.append(0)
        generator_matrix.append(row)

    return generator_matrix


def transform_to_canonical_form(generator_matrix):
    canonical_form = np.concatenate(
        (np.eye(len(generator_matrix[0])), np.array(generator_matrix).T), axis=1)
    pivot_columns = []

    for i in range(len(generator_matrix[0])):
        for j in range(len(generator_matrix)):
            if canonical_form[j][i] == 1:
                pivot_columns.append(canonical_form[:, i])
                break

    pivot_columns = np.array(pivot_columns).T
    canonical_form = pivot_columns

    return canonical_form


def generate_parity_check_matrix(canonical_form):
    parity_check_matrix = -1 * canonical_form[:, len(canonical_form[0]):].T
    return parity_check_matrix


n = 31
k = 26

generator_matrix = generate_generator_matrix(n, k)
print("Generator Matrix:")
for row in generator_matrix:
    print(row)

canonical_form = transform_to_canonical_form(generator_matrix)
parity_check_matrix = generate_parity_check_matrix(canonical_form)

print("\nCanonical Form:")
print(canonical_form)

print("\nParity Check Matrix of Canonical Form:")
print(parity_check_matrix)
