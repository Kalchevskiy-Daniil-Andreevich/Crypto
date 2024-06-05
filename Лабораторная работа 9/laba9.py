class LempelZiv:
    def __init__(self, window_size=(10, 10)):
        self.window_size = window_size

    def compress(self, data):
        window_size = self.window_size
        compressed_data = []
        position = 0
        while position < len(data):
            window = data[max(0, position - window_size[0]):position]
            lookahead = data[position:position + window_size[1]]
            match = self.find_longest_match(window, lookahead)
            if match:
                compressed_data.append((True, match[0], match[1]))
                position += match[1]
            else:
                compressed_data.append((False, data[position]))
                position += 1
        return compressed_data

    def decompress(self, compressed_data):
        decompressed_data = []
        for token in compressed_data:
            if token[0]:
                offset, length = token[1], token[2]
                decompressed_data.extend(decompressed_data[-offset:][:length])
            else:
                decompressed_data.append(token[1])
        return ''.join(decompressed_data)

    def find_longest_match(self, window, lookahead):
        best_match = None
        for i in range(len(lookahead), 0, -1):
            sub = lookahead[:i]
            index = window.rfind(sub)
            if index != -1:
                return (len(window) - index, len(sub))
        return best_match


def calculate_efficiency(original_size, compressed_size):
    R1 = ((original_size - compressed_size) / original_size) * 100
    R2 = (1 - R1 / 100) * 100
    return R1, R2


def main():
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla facilisi."

    for window_size in [(20, 5)]:
        lz = LempelZiv(window_size=window_size)

        compressed_data = lz.compress(text)

        original_size = len(text)
        compressed_size = len(compressed_data)

        R1, R2 = calculate_efficiency(original_size, compressed_size)

        print(f"Window Size: {window_size}")
        print(f"Original Text Length: {original_size}")
        print(f"Compressed Data Length: {compressed_size}")
        print(f"Compression Efficiency (R1): {R1:.2f}%")
        print(f"Decompression Efficiency (R2): {R2:.2f}%")
        print()


if __name__ == "__main__":
    main()
