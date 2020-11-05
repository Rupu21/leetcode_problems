def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, i in enumerate(nums[:-1]):
            j = target - i 
            try:
                return [idx, nums.index(j, idx+1)]
            except: pass
        
