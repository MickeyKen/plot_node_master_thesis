#!/usr/bin/python
import matplotlib.pyplot as plt

single_agent_path = 'data/env_max_200_output_test_0105_1.txt'
multi_agent_path = 'data/param_UD-v95_output.txt'
isServiceCount = True

ACTOR_NUM = 3
AVERAGE_NUM = 100


def calculate_multi_agent():
    rewards = [[] for j in range(ACTOR_NUM)]
    average_rewards = [[] for j in range(ACTOR_NUM)]

    return_rewards  = []
    return_eps = []

    rewards_sum = [[] for j in range(ACTOR_NUM)]

    eps = [[] for j in range(ACTOR_NUM)]
    average_eps = [[] for j in range(ACTOR_NUM)]

    epsilons = [[] for j in range(ACTOR_NUM)]

    flag = 0

    count = 0
    sums= 0.0

    with open(multi_agent_path) as f:

        for s_line in f:
            eps_num = int(s_line.split(',')[0])
            actor_num = int(s_line.split(',')[1])
            reward = int(s_line.split(',')[5])
            epsilon = float(s_line.split(',')[4])
            # print eps_num,actor_num, reward

            rewards[actor_num].append(reward)
            eps[actor_num].append(eps_num)
            epsilons[actor_num].append(epsilon)

            if eps_num % AVERAGE_NUM == 0 and eps_num > 0:
                average_rewards[actor_num].append(sum(rewards_sum[actor_num]) / len(rewards_sum[actor_num]))
                average_eps[actor_num].append(eps_num)
                rewards_sum = [[0] for j in range(ACTOR_NUM)]
            else:
                rewards_sum[actor_num].append(reward)



    for index in range(min(len(v) for v in average_rewards)):
        sums = 0.0
        for n in range(actor_num):
            sums += average_rewards[n][index]
        sums = sums / float(ACTOR_NUM)
        return_rewards.append(sums)
        return_eps.append(index*AVERAGE_NUM)


    return return_rewards, return_eps


def calculate_single_agent():
    xp = []
    yp = []
    yp2 = []
    average_xp = []
    average_yp = []
    average_yp2 = []

    flag = 0
    sum1 = 0
    sum2 = 0

    count = 0
    with open(single_agent_path) as f:
        xp.append(0)
        yp.append(0)
        for s_line in f:
            agent = s_line.split(',')[2]
            # print(int(moji.split('.')[0]))
            xp.append(count + 1)
            yp.append(float(agent))

            num10 = count // AVERAGE_NUM

            if num10 == flag:
                sum1 += float(agent)
            else:
                sum1 = sum1 / AVERAGE_NUM
                average_xp.append((flag+1)*AVERAGE_NUM)
                average_yp.append(sum1)
                sum1 = 0
                sum1 += float(agent)
                flag += 1
            count += 1

    return average_yp, average_xp

if __name__ == '__main__':

    # fig = plt.figure()
    fig = plt.figure(figsize=(8.27,3.9), dpi=100)

    plt.ion()
    plt.xlabel('Episode')
    plt.ylabel('Average reward over the 100 last episodes')
    plt.grid()

    cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']

    multi_average_reward, multi_eps = calculate_multi_agent()
    single_average_reward, single_eps = calculate_single_agent()

    plt.plot(multi_eps,multi_average_reward, color="#e41a1c")
    plt.plot(single_eps,single_average_reward, color="#00529a")

    # plt.legend( loc='upper left', borderaxespad=1)
    plt.draw()
    fig.savefig("result_multi_reward.png")
    plt.pause(0)
