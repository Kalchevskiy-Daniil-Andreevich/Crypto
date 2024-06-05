import heapq
from collections import defaultdict


def build_huffman_tree(data):
    freq_dict = defaultdict(int)
    for char in data:
        freq_dict[char] += 1

    heap = [[weight, [char, ""]] for char, weight in freq_dict.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    return heap[0][1:]


def huffman_encoding(data, codes):
    encoded_data = ""
    for char in data:
        encoded_data += codes[char]
    return encoded_data


def huffman_decoding(data, reverse_mapping):
    decoded_data = ""
    code = ""
    for bit in data:
        code += bit
        if code in reverse_mapping:
            decoded_data += reverse_mapping[code]
            code = ""
    return decoded_data


def calculate_efficiency(original_data, compressed_data):
    original_bits = len(original_data) * 8  # ASCII uses 8 bits per character
    compressed_bits = len(compressed_data)
    efficiency = (original_bits - compressed_bits) / original_bits * 100
    return efficiency


surname = "Kalchevskiy"
name = "Daniil"
data = surname + " " + name

huffman_tree = build_huffman_tree(data)
codes = {char: code for char, code in huffman_tree}
encoded_data = huffman_encoding(data, codes)

reverse_mapping = {code: char for char, code in huffman_tree}
decoded_data = huffman_decoding(encoded_data, reverse_mapping)

print("Original data:", data)
print("Encoded data:", encoded_data)
print("Decoded data:", decoded_data)
print("Efficiency:", calculate_efficiency(data, encoded_data), "%")
