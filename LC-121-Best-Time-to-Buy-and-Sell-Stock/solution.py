from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        cur_max = 0
        left, right = 0, 1

        while right < len(prices):
    
            # check if current trade is 
            if prices[right] > prices[left]:
                cur_max = max(cur_max, prices[right] - prices[left])
            else:
                left = right
            
            # move to next number
            right+=1

        print(left, right)
        return cur_max



def test():
    
    test_runner = Solution()

    test_cases = [
        [1,2,1, 4,3,7, 34, 3, 2],
        [1,2,3,4,5,6,7],
        [7,6,5,4,3,2,1],
        [2,1],
        [2,1,2,0,1]

    ]


    for test_array in test_cases:
        print(test_array, test_runner.maxProfit(test_array))



test()