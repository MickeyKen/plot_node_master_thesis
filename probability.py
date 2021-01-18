#!/usr/bin/python
import matplotlib.pyplot as plt

path = 'data/param_UD-v95_output.txt'
isServiceCount = True

ACTOR_NUM = 3
AVERAGE_NUM = 100

if __name__ == '__main__':

    collision = [[] for j in range(ACTOR_NUM)]
    average_collision = []

    success = [[] for j in range(ACTOR_NUM)]
    average_success = []

    no_action = [[] for j in range(ACTOR_NUM)]
    average_no_action = []

    eps = []
    average_eps = []

    epsilons = [[] for j in range(ACTOR_NUM)]

    flag = 0

    count = 0

    fig = plt.figure(figsize=(8.27,3.9), dpi=100)

    plt.ion()
    plt.xlabel('Episode')
    # plt.ylabel('P')
    plt.grid()

    cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']

    with open(path) as f:

        for s_line in f:
            eps_num = int(s_line.split(',')[0])
            actor_num = int(s_line.split(',')[1])
            step = int(s_line.split(',')[3])
            reward = float(s_line.split(',')[5])
            if step < 150 and reward < -200:
                collision[actor_num].append(1.0)
                success[actor_num].append(0.0)
                no_action[actor_num].append(0.0)
            elif step < 150 and reward > 0:
                collision[actor_num].append(0.0)
                success[actor_num].append(1.0)
                no_action[actor_num].append(0.0)
            else:
                collision[actor_num].append(0.0)
                success[actor_num].append(0.0)
                no_action[actor_num].append(1.0)

        collision_sum = 0.0
        success_sum = 0.0
        no_action_sum = 0.0
        average_collision_sum = 0.0
        average_success_sum = 0.0
        average_no_action_sum = 0.0
        count = 1
        for index in range(min(len(v) for v in collision)):
            collision_sum = 0.0
            success_sum = 0.0
            no_action_sum = 0.0
            for n in range(ACTOR_NUM):
                collision_sum += collision[n][index]
                success_sum += success[n][index]
                no_action_sum += no_action[n][index]

            average_collision_sum += collision_sum / float(ACTOR_NUM)
            average_success_sum += success_sum / float(ACTOR_NUM)
            average_no_action_sum += no_action_sum / float(ACTOR_NUM)

            if index % AVERAGE_NUM == 0 and index > 0:
                average_eps.append(count*AVERAGE_NUM)
                average_collision.append(average_collision_sum / float(AVERAGE_NUM))
                average_success.append(average_success_sum / float(AVERAGE_NUM))
                average_no_action.append(average_no_action_sum / float(AVERAGE_NUM))
                average_collision_sum = 0.0
                average_success_sum = 0.0
                average_no_action_sum = 0.0
                count += 1

            eps.append(index + 1)


        plt.plot(average_eps, average_collision, color='r', label="collision")
        plt.plot(average_eps, average_success, color='g', label="success")
        plt.plot(average_eps, average_no_action, color='b', label="no_action")

        plt.legend( loc='upper left', borderaxespad=1)
        plt.draw()
        fig.savefig("result_multi_probability.png")
        plt.pause(0)
