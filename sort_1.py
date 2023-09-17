import random

def create_matrix(M):
    matrix = [[random.randint(1, 50) for _ in range(M)] for _ in range(M)]
    return matrix

def sort_matrix(matrix):
    column_sums = [sum(col) for col in zip(*matrix)]

    for i in range(len(matrix[0])):
        if i % 2 == 0:
            matrix.sort(key=lambda x: x[i])
        else:
            matrix.sort(key=lambda x: x[i], reverse=True)

    sorted_column_sums = [sum(col) for col in zip(*matrix)]

    return matrix, sorted_column_sums

def print_matrix(matrix, column_sums):
    for row in matrix:
        print("\t".join(map(str, row)))
    print("-" * (8 * len(matrix[0]) - 1))
    print("\t".join(map(str, column_sums)))

if __name__ == "__main__":
    M = int(input("Enter the size of the matrix M (greater than 5): "))
    if M <= 5:
        print("The size of the matrix should be greater than 5.")
    else:
        matrix = create_matrix(M)
        print("Initial matrix:")
        print_matrix(matrix, [sum(col) for col in zip(*matrix)])

        sorted_matrix, sorted_column_sums = sort_matrix(matrix)
        print("\nSorted matrix:")
        print_matrix(sorted_matrix, sorted_column_sums)
