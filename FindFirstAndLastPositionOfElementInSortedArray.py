class Solution:
    def searchRange(self, nums, target: int):
        

        first_index = -1
        second_index = -1


        for i in range(len(nums)):
            if first_index != -1 and second_index != -1:
                break
            if nums[i] == target:
                if first_index == -1:
                    first_index == i
                elif second_index == -1:
                    second_index = i
                
        return [first_index, second_index]


test = Solution()
print(test.searchRange([5,7,7,8,8,10], 8))
