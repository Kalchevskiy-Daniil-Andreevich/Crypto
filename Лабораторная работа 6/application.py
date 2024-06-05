import numpy as np
import random


class HammingCode:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.G = self.generate_generator_matrix()

    def generate_generator_matrix(self):
        p = self.n - self.k
        identity = np.eye(self.k, dtype=int)
        parity = np.random.randint(2, size=(self.k, p))
        return np.concatenate((identity, parity), axis=1)

    def encode(self, message):
        return np.dot(message, self.G) % 2

    def decode(self, received):
        H = np.concatenate((np.eye(self.n - self.k, dtype=int),
                            np.transpose(self.G[:, self.k:])), axis=1)
        syndrome = np.dot(received, np.transpose(H)) % 2
        error_position = np.packbits(syndrome.flatten())
        if np.any(error_position):
            error_position = int(error_position[0])
            if error_position < len(received):
                received[error_position] = 1 - received[error_position]
        return received[:self.k]


def generate_message(length):
    return np.random.randint(2, size=length)


def introduce_errors(message, error_length):
    error_positions = random.sample(range(len(message)), error_length)
    for position in error_positions:
        message[position] = 1 - message[position]
    return message


def main():
    n = 6  # число столбцов в матрице
    k = 5  # длина информационного слова, бит
    message_length = 15  # длина сообщения, байт
    error_lengths = [3, 4, 5]  # длины пакета ошибок
    num_situations = 30  # количество случайных ситуаций

    hamming_code = HammingCode(n, k)

    for error_length in error_lengths:
        print(f"Error Length: {error_length}")
        total_errors_corrected = 0
        total_errors = 0
        for _ in range(num_situations):
            original_message = generate_message(k)

            encoded_message = hamming_code.encode(original_message)
            transmitted_message = introduce_errors(
                encoded_message, error_length)
            decoded_message = hamming_code.decode(transmitted_message)

            errors_corrected = np.sum(
                np.abs(original_message - decoded_message))
            total_errors_corrected += errors_corrected
            total_errors += error_length

            print("Original Message:", original_message)
            print("Transmitted Message:", transmitted_message)
            print("Decoded Message:", decoded_message)
            print("Errors Corrected:", errors_corrected)
            print()

        print("Total Errors Corrected:", total_errors_corrected)
        print("Total Errors Introduced:", total_errors)
        print("Efficiency:", 1 - (total_errors_corrected / total_errors))
        print()


if __name__ == "__main__":
    main()
