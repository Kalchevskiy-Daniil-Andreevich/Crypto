from collections import defaultdict


class ArithmeticCompressor:
    def __init__(self):
        self.low = 0
        self.high = 1
        self.range = 1

    def compress(self, message):
        frequencies = defaultdict(int)
        for symbol in message:
            frequencies[symbol] += 1

        cumulative_frequency = defaultdict(int)
        cumulative_low = 0
        for symbol, freq in sorted(frequencies.items()):
            cumulative_frequency[symbol] = cumulative_low
            cumulative_low += freq / len(message)

        for symbol in message:
            symbol_range = cumulative_frequency[symbol], cumulative_frequency[symbol] + \
                frequencies[symbol] / len(message)
            self.high = self.low + self.range * symbol_range[1]
            self.low = self.low + self.range * symbol_range[0]
            self.range = self.high - self.low

        return (self.low + self.high) / 2

    def decompress(self, compressed_value, original_length, frequencies):
        decompressed_message = ""
        cumulative_frequency = defaultdict(int)
        cumulative_low = 0
        for symbol, freq in sorted(frequencies.items()):
            cumulative_frequency[symbol] = cumulative_low
            cumulative_low += freq / original_length

        while len(decompressed_message) < original_length:
            for symbol, freq in sorted(frequencies.items()):
                symbol_range = cumulative_frequency[symbol], cumulative_frequency[symbol] + \
                    freq / original_length
                if symbol_range[0] <= compressed_value < symbol_range[1]:
                    decompressed_message += symbol
                    self.high = self.low + self.range * symbol_range[1]
                    self.low = self.low + self.range * symbol_range[0]
                    self.range = self.high - self.low
                    break

        return decompressed_message


if __name__ == "__main__":
    compressor = ArithmeticCompressor()

    message_1 = "seedbank"
    compressed_value_1 = compressor.compress(message_1)
    print("Compressed value for message 1:", compressed_value_1)
    decompressed_message_1 = compressor.decompress(compressed_value_1, len(
        message_1), {char: message_1.count(char) for char in set(message_1)})
    print("Decompressed message 1:", message_1)

    message_2 = "seedbankcreativity"
    compressed_value_2 = compressor.compress(message_2)
    print("Compressed value for message 2:", compressed_value_2)
    decompressed_message_2 = compressor.decompress(compressed_value_2, len(
        message_2), {char: message_2.count(char) for char in set(message_2)})
    print("Decompressed message 2:", message_2)
