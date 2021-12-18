'''
8퀸 문제 (8개의 퀸이 서로 공격하여 잡을 수 없도록 8x8 체스판에 퀸을 배치하는 문제)

규칙 1. 각 열에 퀸을 1개만 배치
규칙 2. 각 행에 퀸을 1개만 배치
규칙 3. 대각선 방향으로 퀸이 겹치지 않아야 한다.
참고) 퀸은 체스판에서 가로, 세로, 대각선 어디든지 8개의 방향으로 직선 이동해서 상대를 잡을 수 있다.
'''


# 모든 열에 퀸이 모두 배치되면 출력하는 함수
def put() -> None:
    for i in range(8):
        for j in range(8):
            print(f'{"■" if pos[i] == j else "□"}', end=' ')
        print()
    print()


# 체스판에 퀸을 세팅
def set(i: int) -> None:
    # 1-1. 규칙1을 적용하기 위해 반복문을 돌면서
    for j in range(8):
        # 2-1. 규칙 2를 적용하기 위해 플래그 추가 (필요하지 않은 분기를 없애서 불필요한 작업을 줄이는 한정 작업을 실시한다.)
        if flag[j] == 0 and flag2[i + j] == 0 and flag3[i - j + 7] == 0:
            pos[i] = j  # 1-2. 퀸을 체스판 모든 열에 배치

            if i == 7:  # 1-3. 모든 열에 퀸이 배치 되었다면 출력하고,
                put()
            else:  # 1-4. 아니라면 재귀로 다음 열에 배치
                flag[j] = flag2[i + j] = flag3[i - j + 7] = 1
                set(i + 1)
                flag[j] = flag2[i + j] = flag3[i - j + 7] = 0


# i: 열 j: 행 가정
flag = [0] * 8
# 대각선 조건 p.216 참고
flag2 = [0] * 15
flag3 = [0] * 15
pos = [0] * 8
set(0)
