"""
https://leetcode.com/problems/validate-binary-tree-nodes/?envType=daily-question&envId=2023-10-17

Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true

Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false

Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false
"""
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # ensuring single parent
        c2p = {}
        for i in range(n):
            if leftChild[i] != -1 and leftChild[i] in c2p:
                return False
            c2p[leftChild[i]] = i
            if rightChild[i] != -1 and rightChild[i] in c2p:
                return False
            c2p[rightChild[i]] = i
        
        root = -1
        for i in range(n):
            if i not in c2p:
                if root != -1:
                    # found another root
                    return False
                root = i
        
        # connected component should be 1
        q = deque()
        seen = set()

        q.append(root)
        # print(f'{root=}')

        while q:
            i = q.popleft()
            if i in seen:
                return False
            seen.add(i)
            if leftChild[i] != -1:
                q.append(leftChild[i])
            if rightChild[i] != -1:
                q.append(rightChild[i])
        
        return len(seen) == n

