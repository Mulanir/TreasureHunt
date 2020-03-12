def get_treasure_solver(matrix_array):
    def treasure_solver(key=11):
        row, column = key // 10 - 1, key % 10 - 1
        next_key = matrix_array[row][column]

        return [key] if key == next_key else [key] + treasure_solver(next_key)

    return treasure_solver
