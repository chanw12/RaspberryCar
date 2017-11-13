from carModule import *
import time


def lineTracing():
    current_dis = 100
    standard_dis = 25
    start_time = 0

    while True:
        # set OTD ~ OTE
        output = get_DBACE()
        OTD, OTB, OTA, OTC, OTE = output[0], output[1] ,output[2], output[3], output[4]

        # find obstacle
        if current_dis <= standard_dis:
            go_forward_diff(90, 0)
            sleep(0.5)
            go_forward_diff(20, 50)
            sleep(1)

            # =====================================
            # Code: SwingTurn(Right) => 직진 => SwingTurn(Left)
            # go_forward_diff(90, 0)
            # sleep(0.5)
            # go_forward_diff(45, 45)
            # sleep(1)
            # go_forward_diff(0, 90)
            # sleep(0.5)
            # go_forward_diff(45, 45)
            # sleep(1)
            # go_forward_diff(0, 90)
            # sleep(0.5)
            # go_forward_diff(45, 45)
            # sleep(0.5)
            # =====================================

            while get_DBACE()[2] == 1:
                continue
            current_dis = 100

        # =============== getDistance ===============
        if start_time == 0:
            start_time = time.time()
            getDistance1()
        if time.time() - start_time >= 0.5:
            current_dis = getDistance2()
            start_time = 0

        print(output, current_dis)

        # Line Tracing Start ##############################
        # 라인 이탈 (All White)
        if OTD == 1 and OTB == 1 and OTA == 1 and OTC == 1 and OTE == 1:
            go_forward_diff(5, 90)
        # 감지 불가 (All Black)
        elif OTD == 0 and OTB == 0 and OTA ==0 and OTC == 0 and OTE == 0:
            go_forward_diff(0, 0)
        # 중앙 감지
        elif OTD == 1 and OTB == 1 and OTA == 0 and OTC == 1 and OTE == 1:
            go_forward_diff(45, 45)
        # 왼쪽으로 치우친 중앙 감지
        elif OTB == 0:
            go_forward_diff(20, 55)
        # 오른쪽으로 치우친 중앙 감지
        elif OTC == 0:
            go_forward_diff(55, 20)
        # 왼쪽으로 심하게 치우침
        elif OTD == 0:
            go_forward_diff(5, 90)
        # 오른쪽으로 심하게 치우침
        elif OTE == 0:
            go_forward_diff(90, 5)
        else:
            go_forward_diff(0, 0)

        sleep(0.1)


if __name__ == '__main__':
    try:
        setup()
        lineTracing()
    except KeyboardInterrupt:
        pwm_low()
        GPIO.cleanup()
