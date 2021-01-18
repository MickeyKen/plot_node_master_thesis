#!/usr/bin/python
import matplotlib.pyplot as plt

path = 'data/loss_UD-v95.txt'
AVERAGE_NUM = 100
AVERAGE = False
if __name__ == '__main__':

    actor_num = 2
    a_1 = []
    a_2 = []


    xp = []
    yp = []
    yp2 = []
    average_xp = []
    average_yp = []
    average_yp2 = []
    sum_array = []

    flag = 0
    sum1 = 0
    sum2 = 0

    count = 0

    fig = plt.figure(figsize=(8.27,3.9), dpi=100)

    plt.ion()
    # plt.title('Simple Curve Graph')
    plt.xlabel('Episode')
    plt.ylabel('Losses')
    plt.grid()
    with open(path) as f:
        for s_line in f:
            print s_line.split(' ')[2]
            count += 1
            loss = float(s_line.split(' ')[2])
            xp.append(count)
            yp.append(loss)

            if count % AVERAGE_NUM == 0 and count > 0 and AVERAGE:
                average_yp.append(sum(sum_array) / len(sum_array))
                average_xp.append(count)
                sum_array = []
            else:
                sum_array.append(loss)
        # plt.plot(xp,yp, color="#a9ceec", alpha=0.5)
        plt.plot(xp, yp, color="#00529a")
        plt.draw()
        fig.savefig("result_multi_loss.png")
        plt.pause(0)
