class Matrix:
    def __init__(self, matrix_string):
        self._matrix_string = self.__matrix_string_array(matrix_string) 
        print(self._matrix_string)

    def row(self, index):

        if len(self._matrix_string) == 1:
            return self._matrix_string[0]
        try:
            return self._matrix_string[index-1]
        except:
            raise IndexError

    def column(self, index):
        if len(self._matrix_string) == 1:
            return self._matrix_string[0]
        c = []
        try:
            for i in self._matrix_string:
                c.append(i[index-1])
        except:
            raise IndexError

        return c

    def __matrix_string_array(self, m_string):

        return [[int(f) for f in i.split(" ")] for i in m_string.split('\n')]



if __name__ == "__main__":
    matrix = Matrix('1 2 3\n4 5 6\n7 8 9')
    print(matrix.column(3))
    