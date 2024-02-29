import random


def rock_scissors_paper():
    wins = 0  # 승리 횟수
    losses = 0  # 패배 횟수
    ties = 0  # 무승부 횟수

    while True:
        user_choice = input("가위, 바위, 보 중 하나를 선택하세요: ")

        # 사용자의 선택이 유효한지 확인
        if user_choice not in ['가위', '바위', '보']:
            print("유효한 입력이 아닙니다.")
            continue

        computer_choice = random.choice(['가위', '바위', '보'])

        print(f"사용자: {user_choice}, 컴퓨터: {computer_choice}")

        # 게임 결과 비교
        if user_choice == computer_choice:
            print("무승부!")
            ties += 1
        elif (user_choice == '가위' and computer_choice == '보') or \
             (user_choice == '바위' and computer_choice == '가위') or \
             (user_choice == '보' and computer_choice == '바위'):
            print("사용자 승리!")
            wins += 1
        else:
            print("컴퓨터 승리!")
            losses += 1

        play_again = input("다시 하시겠습니까? (y/n): ").lower()
        if play_again != 'y':
            break

    print("게임을 종료합니다.")
    print(f"승: {wins} 패: {losses} 무승부: {ties}")

rock_scissors_paper()
