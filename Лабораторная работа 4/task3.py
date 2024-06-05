binary_word = "11010101010101111101010101110101"


def calculate_parity_bits(data):
    r = 0
    while 2 ** r < len(data) + r + 1:
        r += 1

    parity_bits = [0] * r

    for i in range(r):
        mask = 2 ** i
        for j in range(len(data)):
            if j & mask:
                parity_bits[i] ^= int(data[j])

    return parity_bits


def generate_hamming_code(binary_word):
    parity_bits = calculate_parity_bits(binary_word)

    code_word = list(binary_word)
    for i, bit in enumerate(parity_bits):
        code_word.insert(2 ** i - 1, str(bit))

    return ''.join(code_word)


code_word_Xn = generate_hamming_code(binary_word)
print("Codeword Xn:", code_word_Xn)
