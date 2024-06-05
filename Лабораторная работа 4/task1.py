def binary_to_matrix(binary_string):
    matrix = []
    for i in range(0, len(binary_string), 8):
        row = [int(bit) for bit in binary_string[i:i+8]]
        matrix.append(row)
    return matrix


binary_word = "11010101010101111101010101110101"

matrix = binary_to_matrix(binary_word)
for row in matrix:
    print(row)
