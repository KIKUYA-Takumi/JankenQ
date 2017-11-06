import random
state = ['win', 'draw', 'lose']
action = ['gu', 'choki', 'pa']
reward = {'win': 1, "draw": 0, 'lose': -1}
alpha = 0.1
gamma = 0.3
epsilon = 0.2
first_state = state[1]
Q_value = {}
for i in state:
    Q_value.update({i:{}})
    for j in action:
        Q_value[i].update({j:1})
def decide_action(state):
    act = ''
    action = ['gu', 'choki', 'pa']
    random_value = random.random()
    if random_value > epsilon:
        for i in Q_value[state].keys():
            if Q_value[state][i] == max(Q_value[state].values()):
                act = i
        return act
    else:
        random_act = random.randint(0, 2)
        return action[random_act]
def judge(player, ai):
    next_state = ''
    if player == 'gu':
        if ai == 'gu':
            next_state = 'draw'
        elif ai == 'pa':
            next_state = 'win'
        elif ai == 'choki':
            next_state = 'lose'
    elif player == 'pa':
        if ai == 'gu':
            next_state = 'lose'
        elif ai == 'pa':
            next_state = 'draw'
        elif ai == 'choki':
            next_state = 'win'
    elif player == 'choki':
        if ai == 'gu':
            next_state = 'win'
        elif ai == 'pa':
            next_state = 'lose'
        elif ai == 'choki':
            next_state = 'draw'
    return next_state
def update_q_value(state, action, next):
    update_part = alpha * (reward[next] + gamma * Q_value[next][max(Q_value[next])] - Q_value[state][action])
    Q_value[state][action] = Q_value[state][action] + update_part
    return Q_value[state][action]
def command():
    print('================================')
    print('グーを出す=' + "'gu'と入力")
    print('パーを出す=' + "'pa'と入力")
    print('チョキを出す=' + "'choki'と入力")
    print('終了する' + "'stop'と入力")
    print('Q値を表示する' + "'score'と入力")
    print('================================')
def main():
    now_state = first_state
    command()
    while True:
        print('じゃんけん:', end='')
        janken = input()
        if janken == 'gu':
            print('あなたの出した手', janken)
        elif janken == 'choki':
            print('あなたの出した手', janken)
        elif janken == 'pa':
            print('あなたの出した手', janken)
        elif janken == 'stop':
            break
        elif janken == 'score':
            print(Q_value)
            continue
        elif janken == 'command':
            command()
            continue
        else:
            print('まじめにやれ！')
            print('--------------------------------')
            continue
        ai_janken = decide_action(now_state)
        print('AIの出した手', ai_janken)
        next_state = judge(janken, ai_janken)
        before_q_value = Q_value[now_state][ai_janken]
        update_q = update_q_value(now_state, ai_janken, next_state)
        now_state = next_state
        print('AI:',now_state, '/', '更新したQ値:', update_q, '更新前のQ値', before_q_value)
        print('--------------------------------')
if __name__ == '__main__':
    main()