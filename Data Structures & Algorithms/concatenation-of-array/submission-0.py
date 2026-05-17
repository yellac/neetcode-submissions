class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        concat_nums: List[int] = nums.copy()
        for n in nums:
            concat_nums.append(n) 
        return concat_nums