#Time Complexity O(klongN),k = length of values, N = length of arr
class Solution:
    def insertingIndex(self, arr, values):
        def helper(val,arr):
            left = 0
            right = len(arr) - 1
            while left <= right:
                mid = left + (right - left)//2
                if arr[mid] == val:
                    index = mid
                    while arr[index] == val:
                        index -= 1
                    return index + 1
                elif arr[mid] < val:
                    left = mid + 1
                else:
                    right = mid - 1
            index = left
            return index



        result = []
        for val in values:
            index = helper(val, arr)
            result.append(index)
        return result







def main():
    arr = [0,0,0,0,0,1,1,1,1,2,2,5,5,5,8,9,10,11]
    values = [1,4,5,10]
    a = Solution
    result = a.insertingIndex(a,arr, values)
    print(result)

main()
