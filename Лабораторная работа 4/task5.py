def detect_errors(code_word, parity_group_size):
    error_positions = []
    n = len(code_word)
    for i in range(parity_group_size):
        start = i
        end = n
        step = 2 * parity_group_size
        if i >= parity_group_size:
            start = parity_group_size
            end = n - parity_group_size
            step = 2 * parity_group_size - 1
        parity_sum = 0
        for j in range(start, end, step):
            parity_sum += int(code_word[j])
        if parity_sum % 2 == 1:
            error_positions.append(i)
    return error_positions


def correct_errors(code_word, error_positions):
    corrected_word = list(code_word)
    for pos in error_positions:
        corrected_word[pos] = '0' if corrected_word[pos] == '1' else '1'
    return ''.join(corrected_word)


def detect_and_correct_errors(code_word, parity_group_size):
    print("Original codeword:", code_word)
    error_positions = detect_errors(code_word, parity_group_size)
    if error_positions:
        print("Error positions:", error_positions)
        corrected_word = correct_errors(code_word, error_positions)
        print("Corrected word:", corrected_word)
        return corrected_word
    else:
        print("No errors detected.")
        return code_word


code_word = '00111010010101001011111010101010110101'
corrected_word = detect_and_correct_errors(code_word, 3)
