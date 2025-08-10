class Solution:
    def __init__(self, n: int, m: int, matrix: list):
        self.n = n
        self.m = m
        self.matrix = matrix
        self.matrix_sum = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                self.matrix_sum[i][j] = self.matrix_sum[i-1][j] + self.matrix_sum[i][j-1] - self.matrix_sum[i-1][j-1] + self.matrix[i-1][j-1]
    def get_ans(self, x1: int, y1: int, x2: int, y2: int) -> int:
        return self.matrix_sum[x2][y2] - self.matrix_sum[x1 - 1][y2] - self.matrix_sum[x2][y1 - 1] + self.matrix_sum[x1 - 1][y1 - 1]
if __name__ == '__main__':
    n_m = list(map(int, input().split()))
    n = int(n_m[0])
    m = int(n_m[1])
    q = int(n_m[2])
    matrix = []
    for _ in range(n):
        num = list(map(int, input().split()))
        matrix.append(num)
    sol = Solution(n, m, matrix)
    for i in range(q):
        x1, y1, x2, y2 = map(int, input().split())
        print(sol.get_ans(x1, y1, x2, y2))
