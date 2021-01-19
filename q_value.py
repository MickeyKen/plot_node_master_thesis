#!/usr/bin/python
import matplotlib.pyplot as plt

path = 'data/param_UD-v95_output.txt'
isServiceCount = True

ACTOR_NUM = 3
AVERAGE_NUM = 1
LIMIT = 5000

if __name__ == '__main__':

    q_values = [[] for j in range(ACTOR_NUM)]
    average_q_values = [[] for j in range(ACTOR_NUM)]

    q_values_sum = [[] for j in range(ACTOR_NUM)]

    eps = [[] for j in range(ACTOR_NUM)]
    average_eps = [[] for j in range(ACTOR_NUM)]

    epsilons = [[] for j in range(ACTOR_NUM)]

    flag = 0

    count = 0

    plot_q_values = []
    plot_eps = []

    fig = plt.figure(figsize=(8.27,3.9), dpi=100)

    plt.ion()
    plt.xlabel('Episode')
    plt.ylabel('MAX Q-value')

    plt.grid()

    cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']

    with open(path) as f:

        for s_line in f:
            eps_num = int(s_line.split(',')[0])
            actor_num = int(s_line.split(',')[1])
            q_value = float(s_line.split(',')[6])
            epsilon = float(s_line.split(',')[4])
            # print eps_num,actor_num, reward

            q_values[actor_num].append(q_value)
            eps[actor_num].append(eps_num)
            epsilons[actor_num].append(epsilon)

            # if eps_num % 100 == 0 and eps_num > 0:
            #     average_q_values[actor_num].append(sum(q_values_sum[actor_num]) / len(q_values_sum[actor_num]))
            #     average_eps[actor_num].append(eps_num)
            #     q_values_sum = [[0] for j in range(ACTOR_NUM)]
            # else:
            #     q_values_sum[actor_num].append(q_value)

        # for i in range(ACTOR_NUM):
        #     label = "epsilon = "+str(epsilons[0][i])
        #     plt.plot(average_eps[i],average_q_values[i], color=cycle[i], label=label)

        for index in range(min(len(v) for v in q_values)):
            if index*AVERAGE_NUM <= LIMIT:
                sums = 0.0
                for n in range(ACTOR_NUM):
                    sums += q_values[n][index]
                sums = sums / float(ACTOR_NUM)
                plot_q_values.append(sums)
                plot_eps.append(index*AVERAGE_NUM)
        plt.plot(plot_eps,plot_q_values, color="#e41a1c")

        # plt.legend( loc='upper left', borderaxespad=1)
        plt.draw()
        fig.savefig("result_multi_q_value.png")
        plt.pause(0)
