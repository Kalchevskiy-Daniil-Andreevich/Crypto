import time


def burrows_wheeler_encode(data):
    data += '$'
    rotations = [data[i:] + data[:i] for i in range(len(data))]
    sorted_rotations = sorted(rotations)
    bwt_encoded = ''.join(rotation[-1] for rotation in sorted_rotations)
    return bwt_encoded


def burrows_wheeler_decode(encoded_data):
    table = [''] * len(encoded_data)
    for i in range(len(encoded_data)):
        table = sorted(encoded_data[i] + table[i]
                       for i in range(len(encoded_data)))
    decoded_data = next(s for s in table if s.endswith('$'))
    return decoded_data[:-1]


def main():
    blocks = ["Daniil", "Kalchevskiy", "seedbank"]

    for block in blocks:
        ascii_binary = ''.join(format(ord(c), '08b') for c in block[:3])
        print("Binary sequence for first 3 characters of",
              block, ":", ascii_binary)

        start_time = time.perf_counter()
        encoded_data = burrows_wheeler_encode(block)
        forward_time = time.perf_counter() - start_time

        start_time = time.perf_counter()
        decoded_data = burrows_wheeler_decode(encoded_data)
        reverse_time = time.perf_counter() - start_time

        print("Forward transformation:", encoded_data)
        print("Inverse transformation:", decoded_data)
        print("Forward transformation time:", forward_time, "sec.")
        print("Inverse transformation time:", reverse_time, "sec.")
        print("\n")


if __name__ == "__main__":
    main()
