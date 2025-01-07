class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        sum1 = sum(nums[:k])
        max_sum = sum1
        j = k
        while j < len(nums):
            sum1 += nums[j] - nums[j-k]
            max_sum = max(sum1, max_sum)
            j= j+1
        return max_sum/k

    def findMaxAverageMethod2(self, nums: List[int], k: int) -> float:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        sum1 = 0
        max_sum = float('-infinity')
        i ,j = 0,0
        while j < len(nums):
            sum1 += nums[j]
            if j-i+1 ==k:
                max_sum = max(max_sum, sum1)
                sum1 -= nums[i]
                i = i +1                
            j += 1
        return max_sum / k
            

            


        
