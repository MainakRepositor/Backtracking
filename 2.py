def permute(self, nums: List[int]) -> List[List[int]]:
        res = []  # initalize an empty list
        if len(nums) == 1:  # base case
            return [nums[:]]
        
        # recursive call
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)  # for next recursive call
            
            for perm in perms:
                perm.append(n)
                
            res.extend(perms)
            nums.append(n)
            
        return res
