class Item:
    def __init__(self, value):
        self.__value = value

    @property
    def direction(self):
        row = self.__value // 10
        column = self.__value % 10

        return (row, column)
