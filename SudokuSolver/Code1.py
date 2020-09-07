"""
This version of script will generate
unique numbers across rows only. It will
not see the sequence along column wise.
"""

mat_full = [[0,0,0,2,6,0,7,0,1],
            [6,8,0,0,7,0,0,9,0],
            [1,9,0,0,0,4,5,0,0],
            [8,2,0,1,0,0,0,4,0],
            [0,0,4,6,0,2,9,0,0],
            [0,5,0,0,0,3,0,2,8],
            [0,0,9,3,0,0,0,7,4],
            [0,4,0,0,5,0,0,3,6],
            [7,0,3,0,1,8,0,0,0]]

mat_transposed = []
mat_solved = []
num_list = [1,2,3,4,5,6,7,8,9]


def transpose_matrix(matrx):
    """
    This function will create a transposed
    matrix named mat_transposed of the
    given input matrix.
    """
    transposed = zip(*matrx)
    for i in transposed:
        j = list(i)
        mat_transposed.append(j)
        # print(j)


transpose_matrix(mat_full)
# print(mat_transposed)

def possibility_finder(row):
    """
    This function will take input from any
    sudoku row and will return a list of
    numbers excluding the numbers which
    are already present in the working row.
    """
    num_list = [1,2,3,4,5,6,7,8,9]
    for i in row:
        if i != 0:
            num_list.remove(i)
    return num_list


def possibility_enter(row1,row2):
    """
    This function will return a list
    in which the int '0's present
    in the sudoku matrix will be
    replaced with the list values
    from the possibility_finder().
    """
    for i in row2:
        for j in range (len(row1)):
            if row1[j] == 0:
                row1[j] = i
                break
    return row1


def main1(matrx):
    """
    This is the main function which will
    take input from the sudoku matrix
    and create row wise solved sudoku
    named 'mat_solved'.
    """
    for i in matrx:
        p1 = possibility_finder(i)
        p2 = possibility_enter(i,p1)
        mat_solved.append(p2)
        print(p2)


main1(mat_full)
# print(mat_solved)
