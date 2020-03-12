class Matrix:
    __items = {}
    __first_key = 11

    def __init__(self, items_array):
        self.__parse_items_array(items_array)

    def __parse_items_array(self, items_array):
        for row_index, column in enumerate(items_array):
            for column_index, value in enumerate(column):
                key = (row_index + 1) * 10 + column_index + 1
                self.__items[key] = value

    def find_treasure(self):
        result = []
        current_key = self.__first_key

        while True:
            result.append(current_key)
            direction = self.__items[current_key]
            item_key = direction

            if item_key == current_key:
                break

            current_key = item_key

        return result
