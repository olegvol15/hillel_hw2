import random

def create_matrix(M):
    matrix = [[random.randint(1, 50) for _ in range(M)] for _ in range(M)]
    return matrix

def bubble_sort(column, reverse=False):
    n = len(column)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if not reverse:
                if column[j] > column[j + 1]:
                    column[j], column[j + 1] = column[j + 1], column[j]
            else:
                if column[j] < column[j + 1]:
                    column[j], column[j + 1] = column[j + 1], column[j]

def sort_matrix(matrix):
    column_sums = [sum(column) for column in zip(*matrix)]
    
    even_columns = [column for i, column in enumerate(matrix) if i % 2 == 0]
    odd_columns = [column for i, column in enumerate(matrix) if i % 2 != 0]
    
    bubble_sort(column_sums)
    
    for column in even_columns:
        bubble_sort(column, reverse=True)
    
    for column in odd_columns:
        bubble_sort(column)
    
    sorted_matrix = []
    for i in range(len(matrix)):
        if i % 2 == 0:
            sorted_matrix.append(even_columns.pop(0))
        else:
            sorted_matrix.append(odd_columns.pop(0))
    
    return sorted_matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))
    column_sums = [sum(column) for column in zip(*matrix)]
    print("Column sums:", column_sums)

if __name__ == "__main__":
    M = int(input("Enter the size of the matrix M (greater than 5): "))
    if M <= 5:
        print("The size of the matrix should be greater than 5.")
    else:
        matrix = create_matrix(M)
        print("Initial matrix:")
        print_matrix(matrix)
        
        sorted_matrix = sort_matrix(matrix)
        print("\nSorted matrix:")
        print_matrix(sorted_matrix)








