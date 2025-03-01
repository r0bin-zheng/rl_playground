import gymnasium as gym
import numpy as np

# 创建FrozenLake环境
env = gym.make('FrozenLake-v1', desc=None, map_name="4x4", is_slippery=False, render_mode="human")  # is_slippery=False表示不使用随机滑动

# 初始化价值函数
V = np.zeros(env.observation_space.n)
gamma = 0.99  # 折扣因子
theta = 1e-6  # 价值迭代的停止条件

# 定义策略（这里只是为了初始化）
policy = np.zeros([env.observation_space.n, env.action_space.n])


def one_step_lookahead(state, V, gamma):
    """执行一次'单步前瞻'，即计算每个动作的期望回报"""
    A = np.zeros(env.action_space.n)
    for a in range(env.action_space.n):
        for prob, next_state, reward, done, _ in env.P[state][a]:
            A[a] += prob * (reward + gamma * V[next_state])
    return A


# 价值迭代
while True:
    delta = 0
    # 对每个状态进行更新
    for state in range(env.observation_space.n):
        # 进行一次'单步前瞻'
        A = one_step_lookahead(state, V, gamma)
        # 更新价值函数
        best_action_value = np.max(A)
        delta = max(delta, np.abs(best_action_value - V[state]))
        V[state] = best_action_value
    # 如果最大的变化小于阈值，停止迭代
    if delta < theta:
        break

# 输出最终的价值函数
print("Final value function:")
print(V)

# 根据价值函数生成最优策略
for state in range(env.observation_space.n):
    A = one_step_lookahead(state, V, gamma)
    policy[state] = np.eye(env.action_space.n)[np.argmax(A)]

# 输出最优策略
print("Optimal policy:")
print(policy)
