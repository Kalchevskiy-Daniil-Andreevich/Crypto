def binary_to_matrix(binary_string):
    matrix = []
    for i in range(0, len(binary_string), 8):
        row = [int(bit) for bit in binary_string[i:i+8]]
        matrix.append(row)
    return matrix


def calculate_parity_bits(matrix, direction):
    parity_bits = []
    if direction == 2:
        for row in matrix:
            parity_bits.append(sum(row) % 2)
    elif direction == 3:
        for col in zip(*matrix):
            parity_bits.append(sum(col) % 2)
    elif direction == 4:
        for i in range(0, len(matrix), 2):
            for j in range(0, len(matrix[i]), 2):
                block = matrix[i][j:j+2] + matrix[i+1][j:j+2]
                parity_bits.append(sum(block) % 2)
    return parity_bits


binary_word = "11010101010101111101010101110101"
matrix = binary_to_matrix(binary_word)

parity_bits_2 = calculate_parity_bits(matrix, 2)
parity_bits_3 = calculate_parity_bits(matrix, 3)
parity_bits_4 = calculate_parity_bits(matrix, 4)

print(f"Parity bits for two directions: {parity_bits_2}")
print(f"Parity bits for three directions: {parity_bits_3}")
print(f"Parity bits for four directions: {parity_bits_4}")
