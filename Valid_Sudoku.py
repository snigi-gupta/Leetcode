# https://leetcode.com/problems/valid-sudoku/solution/

class Solution:
    def isValidSudoku(self, board):

        row = [{} for _ in range(9)]
        column = [{} for _ in range(9)]
        box = [{} for _ in range(9)]

        for i in range(9):
            for j in range(9):
                value = board[i][j]

                if value != ".":
                    value = int(value)
                    box_index = (i // 3) * 3 + (j // 3)

                    row[i][value] = row[i].get(value, 0) + 1
                    column[j][value] = column[j].get(value, 0) + 1
                    box[box_index][value] = box[box_index].get(value, 0) + 1

                    if row[i][value] > 1 or column[j][value] > 1 or box[box_index][value] > 1:
                        return False

        return True


if __name__ == "__main__":
    obj = Solution()
    print(obj.isValidSudoku(
        board=[["5", "3", ".", ".", "7", ".", ".", ".", "."],
               ["6", ".", ".", "1", "9", "5", ".", ".", "."],
               [".", "9", "8", ".", ".", ".", ".", "6", "."],
               ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
               ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
               ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
               [".", "6", ".", ".", ".", ".", "2", "8", "."],
               [".", ".", ".", "4", "1", "9", ".", ".", "5"],
               [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
