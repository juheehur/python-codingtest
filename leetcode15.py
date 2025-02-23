# Generated from blog post
# Title: Leetcode-15
# Date: 2025-02-23
# Code Block 1
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        result = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1  # 합이 0보다 작으면 왼쪽 포인터를 오른쪽으로 이동
                elif total > 0:
                    right -= 1  # 합이 0보다 크면 오른쪽 포인터를 왼쪽으로 이동
                else:
                    # 합이 0인 경우 결과에 추가
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # 중복된 left와 right 값 건너뛰기
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                    
        return result