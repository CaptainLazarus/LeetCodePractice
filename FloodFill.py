from typing import List
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
            visited = [[False for j in range(len(image[0]))] for i in range(len(image))]
            q = deque()
            
            q.append((sr,sc))
            
            targetColor = image[sr][sc]
            
            # left, right, up, down
            directions = [(0,-1) , (0,1) , (1,0) , (-1,0)]
            
            count = 0
            
            while q:
                count+=1
                nodeLoc = q.popleft()
                # print("Popped "+nodeLoc)
                R,C = nodeLoc[0],nodeLoc[1]
                visited[R][C] = True
                if image[R][C] == targetColor:
                    image[R][C] = newColor
                for i in directions:
                    R1 = R+i[0]
                    C1 = C+i[1]
                    if (R1 < 0) or (R1 >= len(image)) or (C1 < 0) or (C1 >= len(image[0])):
                        continue
                    else:
                        if image[R1][C1] == targetColor:
                            if visited[R1][C1] == False:
                                q.append((R1 , C1))
                # for k in visited:
                #     print(k)
                # print()
            return(image)

a = [[1,0,1],[1,1,0],[1,1,1]]
sr = 1
sc = 1
newColor = 2

s = Solution()
s.floodFill(a,sr,sc,newColor)
print(a)