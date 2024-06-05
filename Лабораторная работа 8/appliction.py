from collections import Counter


def shannon_fano_encode(text):
    freq = Counter(text)
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    symbols = [pair[0] for pair in sorted_freq]
    codes = {}

    def divide_and_assign(symbols, start, end, prefix):
        if start == end:
            return
        if start + 1 == end:
            codes[symbols[start]] = prefix
            return
        total_freq = sum(freq[s] for s in symbols[start:end])
        running_freq = 0
        for i in range(start, end):
            if running_freq * 2 >= total_freq:
                divide_and_assign(symbols, start, i, prefix + '0')
                divide_and_assign(symbols, i, end, prefix + '1')
                break
            running_freq += freq[symbols[i]]

    divide_and_assign(symbols, 0, len(symbols), '')

    encoded_text = ''.join(codes[s] for s in text)
    return encoded_text, codes


def shannon_fano_decode(encoded_text, codes):
    reverse_codes = {v: k for k, v in codes.items()}
    current_code = ''
    decoded_text = ''
    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded_text += reverse_codes[current_code]
            current_code = ''
    return decoded_text


def ascii_encode(text):
    return ''.join(str(ord(char)) for char in text)


def ascii_decode(encoded_text):
    return ''.join(chr(int(encoded_text[i:i+3])) for i in range(0, len(encoded_text), 3))


name = "Daniil Kalchevskiy"
encoded_text, codes = shannon_fano_encode(name)
decoded_text = shannon_fano_decode(encoded_text, codes)

print("Original message:", name)
print("Encoded message:", encoded_text)
print("Decoded message:", decoded_text)

ascii_encoded_text = ascii_encode(name)

shannon_fano_compression_ratio = len(encoded_text) / len(name)
ascii_compression_ratio = len(ascii_encoded_text) / len(name)

print("\nShannon-Fano compression efficiency:", shannon_fano_compression_ratio)
print("ASCII compression efficiency:", ascii_compression_ratio)
