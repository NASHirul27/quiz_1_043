# Muhammad Nasrhirul Haq Putra Najamuddin
# F55122043

class MatrixOperations:
    def __init__(self, matrix):
        self.matrix = matrix

    def find_min_max(self):
        flatten_matrix = [item for row in self.matrix for item in row]
        min_val = min(flatten_matrix)
        max_val = max(flatten_matrix)
        return min_val, max_val

    def transpose_matrix(self):
        transposed_matrix = [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]
        return transposed_matrix

    def multiply_matrices(self, other_matrix):
        result_matrix = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*other_matrix)] for row_a in self.matrix]
        return result_matrix

    def add_matrices(self, other_matrix):
        result_matrix = [[a + b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(self.matrix, other_matrix)]
        return result_matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

if __name__ == "__main__":
    matrix_a = [
        [34, 100, 12],
        [72, 24, 55],
        [61, 20, 19]
    ]

    matrix_operations = MatrixOperations(matrix_a)

    # 1. Menghitung element terbesar dan terkecil
    min_val, max_val = matrix_operations.find_min_max()
    print(f"Min Value: {min_val}, Max Value: {max_val}")

    # 2. Transpose matrix (T)
    transposed_matrix = matrix_operations.transpose_matrix()
    print("\nTranspose Matrix:")
    print_matrix(transposed_matrix)

    # 3. Menghitung perkalian matrix (A) dan (T)
    multiplied_matrix = matrix_operations.multiply_matrices(transposed_matrix)
    print("\nPerkalian Matrix:")
    print_matrix(multiplied_matrix)

    # 4. Menghitung penjumlahan matrix (T) dan (A)
    added_matrix = matrix_operations.add_matrices(transposed_matrix)
    print("\nPenjumlahan Matrix:")
    print_matrix(added_matrix)
