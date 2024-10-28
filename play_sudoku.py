#강사님 코드
def play_sudoku():
    board = generate_sudoku() # 보드 만듦
    solved_board = [row[:] for row in board]  # 정답 보드 복사
    solve_sudoku(solved_board)  # 정답을 구함

    print("스도쿠 게임을 시작합니다!")
    while True: #문제 해결될 때까지 반복문
        print_board(board)
        try: #이상한 값 넣으면 에러 나도록.
            row = int(input("행을 입력하세요 (1-9): ")) - 1  #인덱스가 0부터라서 -1로 맞춰줌.
            col = int(input("열을 입력하세요 (1-9): ")) - 1
            num = int(input("숫자를 입력하세요 (1-9): "))

            if not (0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9):
                print("잘못된 입력입니다. 게임을 종료합니다.")
                break  # 게임을 종료합니다 빼고 continue 넣어도 되는 듯..?

            if board[row][col] != 0:
                print("이미 숫자가 있는 칸입니다. 게임을 종료합니다.")
                break #여기도 continue

            if not is_valid(board, row, col, num):
                print("잘못된 이동입니다. 게임을 종료합니다.")
                break  #여기도 컨티뉴

            board[row][col] = num

            if solved_board[row][col] != num:
                print("정답이 아닙니다. 게임을 종료합니다.")
                break #다시 입력하라고 하고 continue 해야 댐.

            if all(all(cell != 0 for cell in row) for row in board):
                print("축하합니다! 스도쿠를 완료했습니다!")
                print_board(board)
                break

        except ValueError:
            print("유효하지 않은 입력입니다. 숫자를 입력해야 합니다. 게임을 종료합니다.")
            break
