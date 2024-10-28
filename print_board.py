# 강사님 코드
def print_board(board): #2차원 리스트의 보드를 인자로 넣어줌.
  for row in board : # row는 0이 9개 들어간 리스트 하나
    print(" ".join(map(str,row)), end = "\n") # 줄넘김 명시해줌. 사실 안 해줘도 됨.