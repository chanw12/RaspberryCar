from carModule import *

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

    while True:
        output = get_DBACE()
        OTD, OTB, OTA, OTC, OTE = output[0], output[1] ,output[2], output[3], output[4]

        print(output)

        # if OTB == 1 and OTA == 0 and OTC == 1:  # Case1
        #     go_forward_diff(30, 30)
        # elif OTB == 0:  # Case2
        #     go_forward_diff(5, 50)
        # elif OTC == 0:  # Case3
        #     go_forward_diff(50, 5)
        # elif OTD == 0:
        #     go_forward_diff(0, 50)
        # elif OTE == 0:
        #     go_forward_diff(50, 0)

        # 라인 이탈 (All White)
        if OTD == 1 and OTB == 1 and OTA == 1 and OTC == 1 and OTE == 1:
            go_forward_diff(50, 5)
        # 감지 불가 (All Black)
        elif OTD == 0 and OTB == 0 and OTA ==0 and OTC == 0 and OTE == 0:
            go_forward_diff(0, 0)
        # 중앙 감지
        elif OTD == 1 and OTB == 1 and OTA == 0 and OTC == 1 and OTE == 1:
            go_forward_diff(30, 30)
        # 왼쪽으로 치우친 중앙 감지
        elif OTB == 0:
            go_forward_diff(25, 35)
        # 오른쪽으로 치우친 중앙 감지
        elif OTC == 0:
            go_forward_diff(35, 25)
        # 왼쪽으로 심하게 치우침
        elif OTD == 0:
            go_forward_diff(5, 70)
        # 오른쪽으로 심하게 치우침
        elif OTE == 0:
            go_forward_diff(70, 5)
        else:
            go_forward_diff(0, 0)

        sleep(0.1)


if __name__ == '__main__':
    try:
        default_settings()
        lineTracing()
    except KeyboardInterrupt:
        pwm_low()
