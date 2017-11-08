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

        # if OTD == 1 and OTE == 1 and (OTB == 0 or OTA == 0 or OTC == 0):  # Case1
        #     go_forward_diff(50, 50)
        # elif OTC == 1 and OTE == 1:  # Case2
        #     go_forward_diff(20, 50)
        # elif OTD == 1 and OTB == 1:  # Case3
        #     go_forward_diff(50, 20)
        # else:
        #     go_forward_diff(0, 0)

        if OTD == 1 and OTB == 1 and OTA == 1 and OTC == 1 and OTE == 1: # 라인 이탈 (All White)
            go_forward_diff(0, 0)
        elif OTD == 0 and OTB == 0 and OTA ==0 and OTC == 0 and OTE == 0: # 감지 불가 (All Black)
            go_forward_diff(0, 0)
        elif OTD == 1 and OTB == 1 and OTA == 0 and OTC == 1 and OTE == 1:
            go_forward_diff(20, 20)
        elif OTD == 0 and OTB == 1 and OTA == 1 and OTC == 1 and OTE == 1:
            go_forward_diff(5, 20)
        elif OTD == 0 and OTB == 0 and OTA == 1 and OTC == 1 and OTE == 1:
            go_forward_diff(10, 20)
        elif OTD == 0 and OTB == 0 and OTA == 0 and OTC == 1 and OTE == 1:
            go_forward_diff(15, 20)
        elif OTD == 1 and OTB == 0 and OTA == 0 and OTC == 1 and OTE == 1:
            go_forward_diff(17, 20)
        elif OTD == 1 and OTB == 1 and OTA == 0 and OTC == 0 and OTE == 1:
            go_forward_diff(20, 17)
        elif OTD == 1 and OTB == 1 and OTA == 0 and OTC == 0 and OTE == 0:
            go_forward_diff(20, 15)
        elif OTD == 1 and OTB == 1 and OTA == 1 and OTC == 0 and OTE == 0:
            go_forward_diff(20, 10)
        elif OTD == 1 and OTB == 1 and OTA == 1 and OTC == 1 and OTE == 0:
            go_forward_diff(20, 5)
        elif OTD == 1 and OTB == 1 and OTA == 1 and OTC == 0 and OTE == 1:
            go_forward_diff(20, 15)
        elif OTD == 1 and OTB == 0 and OTA == 1 and OTC == 1 and OTE == 1:
            go_forward_diff(15, 20)
        else:
            go_forward_diff(0, 0)


if __name__ == '__main__':
    try:
        default_settings()
        lineTracing()
    except KeyboardInterrupt:
        pwm_low()