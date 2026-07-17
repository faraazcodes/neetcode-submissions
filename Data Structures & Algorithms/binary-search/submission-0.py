class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums) - 1
        while lower <= upper:
            partition = (lower + upper) // 2
            if nums[partition] == target: 
                return partition
            if nums[partition] < target: 
                lower = partition + 1
            elif nums[partition] > target:
                upper = partition - 1
        
        return -1
