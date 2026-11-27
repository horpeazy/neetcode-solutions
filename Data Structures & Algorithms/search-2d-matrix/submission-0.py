class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        row = None

        while top <= bottom:
            mid = (top + bottom) // 2
            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                row = matrix[mid]
                break

        if top > bottom or row is None:
            return False

        left = 0
        right = len(row) - 1

        while left <= right:
            mid = (left + right) // 2
            if target < row[mid]:
                right = mid - 1
            elif target > row[mid]:
                left = mid + 1
            else:
                return True

        return False

        
        
        