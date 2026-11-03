class Solution:
    def binarySearch(self, arr, target):
        left, right = 0, len(arr)-1
        while left <= right:
            mid = (left+right)//2
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                right = mid-1
            else:
                left = mid+1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        top = 0
        bottom = m-1
        while top <= bottom:
            mid = (top+bottom)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                bottom = mid-1
            elif matrix[mid][n-1] < target:
                top = mid+1
            else:
                return self.binarySearch(matrix[mid], target)
        return False