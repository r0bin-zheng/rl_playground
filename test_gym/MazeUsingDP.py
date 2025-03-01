def solve_maze_dp(maze):
    """
    使用动态规划方法求解迷宫问题：统计从左上角到右下角的路径数。
    迷宫用二维列表表示，其中 0 表示通路，1 表示障碍物。
    允许移动方向：右和下。
    """
    n = len(maze)
    m = len(maze[0])

    # dp[i][j] 表示从起点到 (i,j) 的路径数
    dp = [[0] * m for _ in range(n)]

    # 如果起点为障碍，则无解
    if maze[0][0] == 1:
        return 0, dp

    dp[0][0] = 1  # 起点

    # 初始化第一行
    for j in range(1, m):
        if maze[0][j] == 0:
            dp[0][j] = dp[0][j-1]
        else:
            dp[0][j] = 0  # 障碍物位置，路径数为0

    # 初始化第一列
    for i in range(1, n):
        if maze[i][0] == 0:
            dp[i][0] = dp[i-1][0]
        else:
            dp[i][0] = 0  # 障碍物位置，路径数为0

    # 填充其余的 dp 表
    for i in range(1, n):
        for j in range(1, m):
            if maze[i][j] == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            else:
                dp[i][j] = 0  # 障碍物不能通过

    return dp[n-1][m-1], dp

if __name__ == "__main__":
    # 定义一个 4x4 的迷宫
    # 0 表示通路，1 表示障碍物
    maze = [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0]
    ]

    path_count, dp_table = solve_maze_dp(maze)

    print("从起点到终点的路径总数：", path_count)
    print("动态规划表 dp：")
    for row in dp_table:
        print(row)
