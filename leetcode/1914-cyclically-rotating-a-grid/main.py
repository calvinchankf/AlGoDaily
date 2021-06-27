"""
    1st: math
    - similar approach as leetcode54
    - traverse a matrix spirally at every layer
    - rotate each layer by k
    - put the items back

    Time    O(RC + (2R+2C)^2)
    Space   O(RC)
    148 ms, faster than 91.67% 
"""


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        R, C = len(grid), len(grid[0])
        layers = []
        maxLayerCount = min(R//2, C//2)
        for i in range(maxLayerCount):
            temp = self.traverseSpirally(grid, i)
            layers.append(temp)
        for i in range(len(layers)):
            layer = layers[i]
            _k = k % len(layer)
            layer = layer[_k:] + layer[:_k]
            self.putSpirally(layer, grid, i)
        return grid

    def traverseSpirally(self, grid, layerIdx):
        R, C = len(grid), len(grid[0])
        top = layerIdx
        right = C - 1 - layerIdx
        bottom = R - 1 - layerIdx
        left = layerIdx
        layer = []
        # go right
        for j in range(left, right+1):
            layer.append(grid[top][j])
        top += 1
        # go down
        for i in range(top, bottom+1):
            layer.append(grid[i][right])
        right -= 1
        # go left
        if top <= bottom:
            for j in range(right, left-1, -1):
                layer.append(grid[bottom][j])
            bottom -= 1
        # go top
        if left <= right:
            for i in range(bottom, top-1, -1):
                layer.append(grid[i][left])
            left += 1
        return layer

    def putSpirally(self, nums, grid, layerIdx):
        R, C = len(grid), len(grid[0])
        top = layerIdx
        right = C - 1 - layerIdx
        bottom = R - 1 - layerIdx
        left = layerIdx
        # go right
        for j in range(left, right+1):
            grid[top][j] = nums.pop(0)
        top += 1
        # go down
        for i in range(top, bottom+1):
            grid[i][right] = nums.pop(0)
        right -= 1
        # go left
        if top <= bottom:
            for j in range(right, left-1, -1):
                grid[bottom][j] = nums.pop(0)
            bottom -= 1
        # go top
        if left <= right:
            for i in range(bottom, top-1, -1):
                grid[i][left] = nums.pop(0)
            left += 1
