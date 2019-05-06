class Solution:
    def fourSum(self, nums, target: int):
        length = len(nums)
        if length < 4:
            return []
        nums.sort()
        ans = []

        for i in range(length - 3):
            for j in range(i + 1, length - 2):
                start = j + 1
                end = length - 1
                while start < end:
                    temp = nums[i] + nums[j] + nums[start] + nums[end]
                    if temp == target:
                        temp_ans = [nums[i], nums[j], nums[start], nums[end]]
                        if temp_ans not in ans:
                            ans.append([nums[i], nums[j], nums[start], nums[end]])
                        start += 1
                        end -= 1
                    elif temp < target:
                        start += 1
                    elif temp > target:
                        end -= 1

        return ans

if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(Solution().fourSum(nums, target))