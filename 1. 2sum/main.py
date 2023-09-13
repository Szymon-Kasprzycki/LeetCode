"""
Given an array of integers nums and an integer target, return indices
of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.
"""

from typing import List


class Solution:
    def _twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :param nums:  list[int] - list of numbers
        :param target:  int - sum of two numbers in nums
        :return:  list[int] - indexes list of two numbers in nums
        """
        hash_table = {}
        for index, num in enumerate(nums):
            to_find = target - num
            if to_find in hash_table:
                return [hash_table[to_find], index]
            hash_table[num] = index

        return []

    def run_test(self, test: dict[str, any]) -> None:
        """
        :param test:  dict[str, any] - test case
        :return:  None
        """
        numbers = test["input"]
        target = test["target"]
        out = test["output"]
        try:
            result = self._twoSum(numbers, target)
            assert result == out
            print("Test case passed: ", test)
        except AssertionError:
            print("Test case failed: ", test)

    def run_tests(self, test_cases: list[dict[str, any]]) -> None:
        """
        :param test_cases:  list[dict[str, any]] - list of test cases
        :return:  None
        """
        for test in test_cases:
            self.run_test(test)


# Test cases
if __name__ == "__main__":
    tests = [
        {
            "input": ([2, 7, 11, 15]),
            "target": 9,
            "output": [0, 1]
        },
        {
            "input": ([3, 2, 4]),
            "target": 6,
            "output": [1, 2]
        },
        {
            "input": ([3, 3]),
            "target": 6,
            "output": [0, 1]
        }
    ]

    Solution().run_tests(tests)
