from carModule import *
import time

# =======================================
# Base Algorithm (Black is 0, White is 1, x is 'don't care')
# D B A C E
# Case1: Go Straight
# 1 x x x 1 (1 1 0 1 1, 1 0 0 0 1)
# Case2: Go Left
# x x x 1 1 (0 1 1 1 1, 0 0 0 1 1)
# Case3: Go Right
# 1 1 x x x (1 1 0 0 0, 1 1 1 1 0)


def lineTracing():
    current_dis = 100
    standard_dis = 40
    start_time = 0

    while True:
        output = get_DBACE()

        if current_dis <= standard_dis:
            go_forward_diff(90, 0)
            sleep(0.5)
            go_forward_diff(20, 50)
            while get_DBACE()[2] == 1:
                continue
            current_dis = 100
        # =============== getDistance ===============
        if start_time == 0:
            start_time = time.time()
            getDistance_start()
        if time.time() - start_time >= 0.5:
            current_dis = getDistance_end()
            start_time = 0

        print(output, current_dis)

        # 라인 이탈 (All White)
        if output == [1, 1, 1, 1, 1]:
            go_forward_diff(90, 5)
        # 감지 불가 (All Black)
        elif output == [0, 0, 0, 0, 0]:
            go_forward_diff(0, 0)
            break
        # 중앙 감지
        elif output == [1, 1, 0, 1, 1]:
            go_forward_diff(45, 45)
        # 왼쪽으로 치우친 중앙 감지
        elif not output[1]:
            go_forward_diff(20, 55)
        # 오른쪽으로 치우친 중앙 감지
        elif not output[3]:
            go_forward_diff(55, 20)
        # 왼쪽으로 심하게 치우침
        elif not output[0]:
            go_forward_diff(5, 90)
        # 오른쪽으로 심하게 치우침
        elif not output[4]:
            go_forward_diff(90, 5)

        sleep(0.1)


# def avoid():
#     #turn_time = 0.3
#     go_forward_diff(70, 0)
#     move(20, 60)
#     while OTA == 1:
#         continue


if __name__ == '__main__':
    try:
        default_settings()
        lineTracing()
    except KeyboardInterrupt:
        pwm_low()
