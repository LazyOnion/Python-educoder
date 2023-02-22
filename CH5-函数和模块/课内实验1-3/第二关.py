from typing import List

def exist(board: List[List[str]], word: str):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if judger(board,i,j,word,0):
                return True
    return False
 
 
def judger(board,i,j,word,index):
    if index == len(word):
        return True
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[index]:
        return False
    board[i][j] = "*"
    Judge = judger(board,i+1,j,word,index+1) or judger(board,i,j+1,word,index+1) or judger(board,i-1,j,word,index+1) or judger(board,i,j-1,word,index+1) or judger(board,i+1,j+1,word,index+1) or judger(board,i-1,j+1,word,index+1) or judger(board,i+1,j-1,word,index+1) or judger(board,i-1,j-1,word,index+1)
    board[i][j] = word[index]
    return Judge
