from types import TracebackType


class Solution:
    def minJumps(self, arr):
        # 贪心？
        # 每一步的目标是以最小的步数移动最远的距离
        # 但并不能得到最小步数到最后
        # e.g. [100, 404, -23, -23, 100, 23, 23, 23, 3, 404]
        # 最少只需要2步，如果贪心则是5步
        # 穷举->复杂度太高，计算每一步的三种选择（如果有）
        # 从后往前推？
        # e.g. [100, -23, -23, 23, 23, 23, 3, 404, 100, 404]
        # 每一步只需要计算两种选择，向左或者跳转，建立二叉树，然后得到最小层数
        # 最短路径算法？
        inf = float('inf')
        length = len(arr)
        ids = list(range(length))

        A = [[0 if i == j else inf for i in ids] for j in ids]
        for i in ids:
            if i > 0:
                A[i][i-1] = 1
            if i < length - 1:
                A[i][i+1] = 1
            for j, n in enumerate(arr):
                if n == arr[i] and i != j:
                    A[i][j] = 1
        # print(A)
        dist = [A[0][i] for i in ids]
        visited = [True if i == 0 else False for i in ids]

        # equal to: while visited is not all True:
        for _ in ids[1:]:
            min_v, min_id = inf, 0  # find nearest node in dist
            for i in ids[1:]:
                if(not visited[i]) and (dist[i] < min_v):
                    min_id = i
                    min_v = dist[i]
            # added min_id to visited set, and update dist array
            visited[min_id] = True
            # for i in V-S, if w_min_id_i + dist[min_id] < dist[i], update dist[i]
            for i in ids:
                if i != min_id and not visited[i] and (A[min_id][i] + dist[min_id]< dist[i]):
                    dist[i] = A[min_id][i] + dist[min_id]
        return dist[-1]


if __name__ == '__main__':
    arr = [100,-23,-23,404,100,23,23,23,3,404]
    sol = Solution()
    sol.minJumps(arr)

