from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.max_sub_kadane(nums)

    def max_sub_kadane(self, nums: List[int]) -> int:
        """
        Kadane's algorithm inspired version.
        Took a while, and a whole lot of resources to help understand it.
        TODO: Link resources here
        """

        # cur_max : current max from beginning of array to 
        # to any index in array

        # max_overall : overall maximum subarray found
        # may not be equal to cur_max

        # begin by assuming the current max and oveall max
        # is the sum of the subarray containing only first element
        max_overall = cur_max = nums[0]

        # consider the rest of the elements
        # (i.e. we've already dealt with the first above)
        for num in nums[1:]:

            # update cur_max with the new element, 
            # or change it if the new element is larger than the current so far
            cur_max = max(cur_max + num, num)
            
            # update the overall max if our current max is larger
            max_overall = max(max_overall, cur_max)

        return max_overall

    def max_sub_divide_conquer(self, nums: List[int]) -> int:
        """
            Divide-and-conquer version of max subarray problem
            Status: WIP
            TODO: Implement
        """
        return -1


def test():

    test_runner = Solution()

    test_array = [-6, 0, 1, 2 ,3, -1, -2, 3, 1]

    print(test_runner.maxSubArray(test_array))

test()