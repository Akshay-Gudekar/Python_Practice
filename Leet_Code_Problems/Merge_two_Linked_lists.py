# 1. You MUST define what a ListNode is
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 2. A helper function to turn a Python list [] into a Linked List
def create_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for number in arr:
        curr.next = ListNode(number)
        curr = curr.next
    return dummy.next

# 3. A helper function to print the Linked List so you can see the result
def print_list(node):
    result = []
    while node:
        result.append(str(node.val))
        node = node.next
    print(",".join(result))

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        current = dummy
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 or list2
        return dummy.next

# --- EXECUTION ---
sol = Solution()

# Convert regular lists to Linked Lists
l1 = create_linked_list([1, 2, 4])
l2 = create_linked_list([1, 3, 4])

# Now the function will work because l1 and l2 have a '.val'
merged_head = sol.mergeTwoLists(l1, l2)

# Print the result
print_list(merged_head)