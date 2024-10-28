import random

def generate_sudoku():
  puzzle = []
  numbers = [0] *9 + list(range(1,10))

  for _ in range(9): # 행 9개
    row = []
    for _ in range(9): # 열 9개

      rand_int = random.choice(numbers)   # 뽑힐 확률을 조절하기 위해 choice 함수 씀
      # numbers가  0이 9개 들어간 리스트이니 50% 확률로 0이 나옴.
      # rand_int = random.randint(0,9)도 가능한 코드. 0이 나올 확률이 무조건 1/10
      row.append(rand_int)
    puzzle.append(row)

  return puzzle