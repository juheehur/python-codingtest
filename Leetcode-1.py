# Generated from blog post
# Title: [Leetcode] 1. Two Sum
# Date: 2025-02-02
# Code Block 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # number 랑 index 저장용 dictionary 만들기
        num_dict = {}
        
        # target-num값을 complement에 저장해놓고, complement가 num_dict에 있으면 가져오는것 (7,2 가 nums에 있고 타겟이 9라면 9-7인 2 가 nums에 있으니)
        for i, num in enumerate(nums): 
            complement = target - num
           
            if complement in num_dict:
                return [num_dict[complement], i]
            
            # 없으면 num_dict에 저장 
            num_dict[num] = i

#enumerate 쓰면 각 원소의 인덱스(i)와 값(num)을 동시에 얻을 수 있음