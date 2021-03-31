def isValidSudoku(board):
    #check row
    for i in range(9):
        setOfRow = set()
        for ele in board[i]:
            if ele.isdigit() == True:
                if ele not in setOfRow:
                    if 0 < int(ele) < 10:
                        setOfRow.add(ele)
                    else:
                        print("here")
                else:
                    print("Duplicated")
    #check column
    for j in range(9):
        setOfColumn = set()
        for i in range(9):
            if board[i][j] not in setOfColumn:
                if board[i][j].isdigit() == True:
                    if 0 < int(board[i][j]) < 10:
                        setOfColumn.add(board[i][j])
                    else:
                        return False
            else:
                return False
        print(setOfColumn)

    #check 9x9 cube
    setOfBox1 = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] not in setOfBox1:
                if board[i][j].isdigit() == True:
                    if 0 < int(board[i][j]) < 10:
                        setOfBox1.add(board[i][j])
                    else:
                        return False
            else:
                return False
    setOfBox2 = set()
    for i in range(3):
        for j in range(3, 6):
            if board[i][j] not in setOfBox2:
                if board[i][j].isdigit() == True:
                    if 0 < int(board[i][j]) < 10:
                        setOfBox2.add(board[i][j])
                    else:
                        return False
            else:
                return False
    setOfBox3 = set()
    for i in range(3):
        for j in range(6,9):
            if board[i][j] not in setOfBox3:
                if board[i][j].isdigit() == True:
                    if 0 < int(board[i][j]) < 10:
                        setOfBox3.add(board[i][j])
                    else:
                        return False
            else:
                return False
    setOfBox4 = set()
    for i in range(3, 6):
        for j in range(3):
            if board[i][j] not in setOfBox4:
                if board[i][j].isdigit() == True:
                    if 0 < int(board[i][j]) < 10:
                        setOfBox4.add(board[i][j])
                    else:
                        return False
            else:
                return False

    setOfBox5 = set()
    for i in range(3, 6):
        for j in range(3, 6):
            if board[i][j] not in setOfBox5:
                if board[i][j].isdigit() == True:
                    if 0 < int(board[i][j]) < 10:
                        setOfBox5.add(board[i][j])
                    else:
                        return False
            else:
                return False

    setOfBox6 = set()
    for i in range(3, 6):
        for j in range(6, 9):
            if board[i][j] not in setOfBox6:
                if board[i][j].isdigit() == True:
                    if 0 < int(board[i][j]) < 10:
                        setOfBox6.add(board[i][j])
                    else:
                        return False
            else:
                return False

    setOfBox7 = set()
    for i in range(6, 9):
        for j in range(3):
            if board[i][j] not in setOfBox7:
                if board[i][j].isdigit() == True:
                    if 0 < int(board[i][j]) < 10:
                        setOfBox7.add(board[i][j])
                    else:
                        return False
            else:
                return False
    setOfBox8 = set()
    for i in range(6, 9):
        for j in range(3, 6):
            if board[i][j] not in setOfBox8:
                if board[i][j].isdigit() == True:
                    if 0 < int(board[i][j]) < 10:
                        setOfBox8.add(board[i][j])
                    else:
                        return False
            else:
                return False
    setOfBox9 = set()
    for i in range(6, 9):
        for j in range(6, 9):
            if board[i][j] not in setOfBox9:
                if board[i][j].isdigit() == True:
                    if 0 < int(board[i][j])< 10:
                        setOfBox9.add(board[i][j])
                    else:
                        return False
            else:
                return False

    return True

board = [
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))