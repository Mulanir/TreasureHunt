def get_treasure_solver(matrix_array):
    def treasure_solver(key):
        row, column = key // 10 - 1, key % 10 - 1
        next_key = matrix_array[row][column]

        if key == next_key:
            return [key]
        else:
            return [key] + treasure_solver(next_key)

    return treasure_solver
