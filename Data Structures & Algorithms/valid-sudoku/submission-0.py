class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=defaultdict(set)
        col=defaultdict(set)
        boxes=defaultdict(set)
        rows=len(board[0])
        cols=len(board)
        for i in range(rows):
            for j in range(cols):
                num=board[i][j]
                if num==".":
                    continue
                box=(i//3,j//3)
                if num in row[i] or num in col[j] or num in boxes[box]:
                    return False
                
                row[i].add(num)
                col[j].add(num)
                boxes[box].add(num)
        return True
                
                