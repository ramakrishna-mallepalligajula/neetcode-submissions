class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        for num in range(len(nums)):
            ans.append(nums[num])

        result = nums + ans
        return result