# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？


class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0]*(n+1)
        G[0], G[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]

        return G[n]


if __name__ == '__main__':
    sou = Solution()
    print(sou.numTrees(3))