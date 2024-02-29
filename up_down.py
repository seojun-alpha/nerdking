import random


def up_down_game():
    best_attempt = float('inf')  # 이전 게임의 최고 시도 횟수를 저장하기 위한 변수
    play_again = 'y'  # 게임 재시작 여부를 저장하기 위한 변수

    while play_again.lower() == 'y':
        attempts = 0  # 현재 게임의 시도 횟수를 저장하기 위한 변수
        secret_number = random.randint(1, 100)  # 컴퓨터가 생각하는 숫자

        print("숫자를 맞춰보세요! (1에서 100 사이)")

        while True:
            guess = int(input("숫자를 입력하세요: "))
            attempts += 1

            if guess < 1 or guess > 100:  # 입력이 범위를 벗어난 경우
                print("유효한 범위 내의 숫자를 입력하세요.")
                continue

            if guess < secret_number:
                print("업!")
            elif guess > secret_number:
                print("다운!")
            else:
                print(f"맞았습니다! 시도한 횟수: {attempts}")
                if attempts < best_attempt:  # 이전 게임의 최고 시도 횟수보다 현재 게임이 더 좋은 경우
                    best_attempt = attempts

                break

        play_again = input("다시 하시겠습니까? (y/n): ")
        if play_again == 'y':
            print(f"이전 게임 플레이어 최고 시도 횟수: {best_attempt}")

    print("게임을 종료합니다.")


up_down_game()
