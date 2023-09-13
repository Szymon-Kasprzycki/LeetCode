"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

from typing import Optional


class ListNode:
    """
    Definition for singly-linked list.
    """
    def __init__(self, val=0, next_item=None):
        self.val = val
        self.next = next_item

    def __str__(self):
        representation = f"[{self.val}"
        temp = self.next
        if temp is not None:
            while temp is not None:
                representation += f", {temp.val}"
                temp = temp.next
        representation += "]"
        return representation

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False

        if self.next is not None:
            temp = self.next
            other = other.next
            while temp is not None:
                if temp.val != other.val:
                    return False
                temp = temp.next
                other = other.next
        return True


class Solution:
    def _get_number_from_linked_list(self, l: Optional[ListNode]) -> int:
        """
        This function is used to convert a linked list to number using reverse order
        :param l: ListNode - linked list
        :return: int - number from linked list in reverse order
        """
        if l is None:
            return 0
        return l.val + 10 * self._get_number_from_linked_list(l.next)

    def _get_linked_list_from_number(self, n: int, i: int = 0) -> Optional[ListNode]:
        """
        This function is used to convert a number to linked list using reverse order
        :param n:  int - number
        :param i:  int - index
        :return:  ListNode - linked list from number in reverse order
        """
        if n == 0 and i == 0:
            return ListNode(0)
        elif n == 0:
            return None
        return ListNode(n % 10, self._get_linked_list_from_number(n // 10, i + 1))

    def _addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        This function is used to add two numbers represented as linked lists in reverse order
        :param l1:  ListNode - first linked list
        :param l2:  ListNode - second linked list
        :return: ListNode - sum of two numbers represented as linked lists in reverse order
        """
        return self._get_linked_list_from_number(
            self._get_number_from_linked_list(l1) + self._get_number_from_linked_list(l2))

    def _run_test(self, test: dict[str, any]) -> None:
        """
        :param test:  dict[str, any] - test case
        :return:  None
        """
        l1 = test["input"][0]
        l2 = test["input"][1]
        out = test["output"]
        try:
            result = self._addTwoNumbers(l1, l2)
            assert result == out
            print("Test case passed: ", f"{l1} + {l2} != {out}")
        except AssertionError:
            print("Test case failed: ", f"{l1} + {l2} != {out}")

    def run_tests(self, test_cases: list[dict[str, any]]) -> None:
        """
        :param test_cases:  list[dict[str, any]] - list of test cases
        :return:  None
        """
        for test in test_cases:
            self._run_test(test)


if __name__ == "__main__":
    tests = [
        {
            "input": ([ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4)))]),
            "output": ListNode(7, ListNode(0, ListNode(8)))
        },
        {
            "input": ([ListNode(0), ListNode(0)]),
            "output": ListNode(0)
        },
        {
            "input": ([ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))),
                       ListNode(9, ListNode(9, ListNode(9, ListNode(9))))]),
            "output": ListNode(8, ListNode(9, ListNode(9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(
                1))))))))
        }
    ]
    Solution().run_tests(tests)
