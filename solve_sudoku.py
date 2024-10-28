# 강사님 코드
def is_valid(board, row, col, num): #각 행,열,칸에 1~9까지 하나만 있는지 확인하는 3가지 규칙.
    # num은 우리가 넣을 숫자, row는 그 숫자가 들어간 행, col은 그 숫자가 들어간 열.
    # 해당 숫자가 같은 행에 있는지 확인
    for i in range(9):
        if board[row][i] == num: # 해당 행의 모든 인덱스와 비교
            return False # 해당 숫자랑 같으면 틀린 거지.
    #if num in board[row]: #한 줄 코드
        #return False

    # 해당 숫자가 같은 열에 있는지 확인
    if num in [board[i][col] for i in range(9)]: #각 행의 해당 열을 모두 인덱싱해와서 리스트 만듦.
        return False
    #같은 코드인데 여러 줄인 코드
    #for i in range(9):
        #if board[i][col] == num:
            #return False

    # 해당 숫자가 같은 칸(3*3)에 있는지 확인
    # 해당 행,열//3 이 내가 위치한 칸이지. 0부터 시작하면...
    start_row, start_col = (row // 3)*3, (col//3)*3 #박스의 좌측 상단 위치를 표시

    for r in range(start_row, start_row+3): #행방향으로 3줄 체크
        for c in range(start_col, start_col+3): #열방향 3열 체크
            if board[r][c] == num:
                return False

    return True # 위에 세 가지 모두 충족 시

def find_empty_location(board):
    # 보드를 돌면서 0을 찾으면 됨.
    for r in range(9):  #row 돌기
        for c in range(9): #컬럼 돌기
            if board[r][c] == 0: #(r,c)자리의 값. 이중 인덱싱임.  아 리스트 중첩이니까 되겠네
                return r, c # 튜플 형태로 받음. ,있으면 튜플이당
    return None

def solve_sudoku(board):
    # 빈 위치 찾기
    empty_loc = find_empty_location(board) #튜플로 나옴.

    if not empty_loc: #빈 위치가 없다
        return True #보드가 다 채워진 거니까 True 반환

    row, col = empty_loc #튜플 값 받을 변수 지정

    for num in range(1, 10): #1부터 9까지
        if is_valid(board,row,col,num) == True:
            board[row][col] = num # 1부터 9까지 값을 넣어준다.
          #해결이 안되는 보드인 경우#
          ###############3# 함수 안에 본인이 들어감.. >> 재귀 함수!  ###############
            if solve_sudoku(board) == True:
                return True
            else:
                board[row][col] = 0  #풀 수 없는 스도쿠가 되었으니 다시 0으로 지워준다.
          ########################################33
    return False