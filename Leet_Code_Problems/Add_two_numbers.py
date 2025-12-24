

# My Logic
class Solution(object):
    def addTwoNumbers(self, l1, l2):

        new_l1 =  int("".join(map(str, l1[::-1]))) #we use map when we want to change data type
        #when we have a list of numbers and need to perform the same calculation on all of them e.g squared = list(map(lambda x: x**2, numbers))
        new_l2 =  int("".join(map(str, l2[::-1])))
        sum_of_list = new_l1+new_l2
        result = [int(i) for i in str(sum_of_list)[::-1]]
        # temp_str = str(sum_of_list)[::-1]
        # result = []
        # for i in temp_str:
        #     number = int(i)
        #     result.append(number)
        return result


l1=[2,4,3]
l2=[5,6,4]
sol = Solution()
print(sol.addTwoNumbers(l1,l2))

# # Using link list
# """
# PROBLEM DESCRIPTION:
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in REVERSE order (e.g., 342 is stored as 2 -> 4 -> 3).
# Each of their nodes contains a single digit. Add the two numbers and return
# the sum as a linked list.
#
# Example:
# Input:  (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Math:   342 + 465 = 807
# Output: 7 -> 0 -> 8
# """
#
#
# # Definition for singly-linked list node (Provided by LeetCode).
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
#
# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         # 1. Initialize a "dummy" node. This acts as a fixed starting point.
#         # We will attach our result digits to this dummy node.
#         dummy = ListNode(0)
#
#         # 2. 'curr' (current) is a pointer that starts at the dummy node.
#         # It will move forward as we add each digit to our new list.
#         curr = dummy
#
#         # 3. 'carry' stores the value when the sum of two digits is 10 or more.
#         carry = 0
#
#         # 4. Loop as long as there is still a digit in l1, l2, OR a remaining carry.
#         while l1 or l2 or carry:
#             # 5. Extract the digit from l1 and l2.
#             # If a list has run out of nodes, use 0 as the value.
#             v1 = l1.val if l1 else 0
#             v2 = l2.val if l2 else 0
#
#             # 6. Calculate the total for this "column" (digit position).
#             # Total = Digit from l1 + Digit from l2 + Carry from previous column.
#             total = v1 + v2 + carry
#
#             # 7. Update the carry for the next position.
#             # Example: If total is 13, 13 // 10 = 1 (the carry).
#             carry = total // 10
#
#             # 8. Get the single digit for the current position.
#             # Example: If total is 13, 13 % 10 = 3 (the digit we store).
#             # Create a new Node with this digit and link it to our result list.
#             curr.next = ListNode(total % 10)
#
#             # 9. Move the 'curr' pointer forward to the node we just created.
#             curr = curr.next
#
#             # 10. Advance l1 and l2 to the next nodes in their chains.
#             # If we've reached the end of a list, keep it as None.
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None
#
#         # 11. The dummy node's value (0) is not part of our answer.
#         # Our real answer starts at dummy.next.
#         return dummy.next