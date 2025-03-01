import math

# 定义迷宫：0 表示可以通行，1 表示障碍
maze = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

n = 4  # 迷宫大小为 4x4

# dp数组用于记录从起点 (0,0) 到各点的最小步数，初始值设为无穷大
dp = [[math.inf for _ in range(n)] for _ in range(n)]
# prev数组用于记录每个位置的前驱坐标，方便回溯最优路径
prev = [[None for _ in range(n)] for _ in range(n)]

# 起点如果可走，则步数为0
if maze[0][0] == 0:
    dp[0][0] = 0
else:
    print("起点被障碍物占据，无法走出迷宫！")
    exit()

# 利用动态规划更新状态：
# 由于只允许向右和向下移动，所以遍历顺序为从左到右，从上到下
for i in range(n):
    for j in range(n):
        # 如果当前位置是障碍，跳过
        if maze[i][j] == 1:
            continue

        # 尝试向右移动
        if j + 1 < n and maze[i][j + 1] == 0:
            if dp[i][j] + 1 < dp[i][j + 1]:
                dp[i][j + 1] = dp[i][j] + 1
                prev[i][j + 1] = (i, j)  # 记录前驱

        # 尝试向下移动
        if i + 1 < n and maze[i + 1][j] == 0:
            if dp[i][j] + 1 < dp[i + 1][j]:
                dp[i + 1][j] = dp[i][j] + 1
                prev[i + 1][j] = (i, j)  # 记录前驱

# 判断终点是否可达
if dp[n - 1][n - 1] == math.inf:
    print("无法走出迷宫！")
else:
    # 回溯最优路径，从终点回溯到起点
    path = []
    i, j = n - 1, n - 1
    while (i, j) is not None:
        path.append((i, j))
        # 如果到达起点则结束
        if (i, j) == (0, 0):
            break
        (i, j) = prev[i][j]
    path.reverse()  # 反转路径，使之从起点到终点

    print("最优路线：")
    for pos in path:
        print(pos)
