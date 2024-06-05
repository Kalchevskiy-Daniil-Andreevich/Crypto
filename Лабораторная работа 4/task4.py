import random


def generate_error(code_word):
    n = len(code_word)

    error_count = random.randint(1, n)

    error_positions = random.sample(range(n), error_count)

    error_code_word = list(code_word)
    for pos in error_positions:
        error_code_word[pos] = '0' if error_code_word[pos] == '1' else '1'

    return ''.join(error_code_word)


code_word = '00111010010101001011111010101010110101'

error_code_word = generate_error(code_word)

print("Original codeword:", code_word)
print("Error codeword:", error_code_word)
