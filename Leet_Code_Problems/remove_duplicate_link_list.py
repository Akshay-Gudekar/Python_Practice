from typing import Optional


# 1. Define the Node structure
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 2. The Solution class containing the logic
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current and current.next:
            if current.val == current.next.val:
                # Found a duplicate: change the pointer to skip the next node
                current.next = current.next.next
            else:
                # No duplicate: move the 'current' pointer forward
                current = current.next

        return head


# 3. Helper functions to make testing easier
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_linked_list(head):
    elements = []
    while head:
        elements.append(str(head.val))
        head = head.next
    print(" -> ".join(elements) if elements else "Empty List")


# 4. Main execution block
if __name__ == "__main__":
    # Create an instance of the solution
    sol = Solution()

    # Test Case: [1, 1, 2, 3, 3]
    test_data = [1, 1, 2, 3, 3]
    linked_list_head = create_linked_list(test_data)

    print("Original List:")
    print_linked_list(linked_list_head)

    # Run the function
    result = sol.deleteDuplicates(linked_list_head)

    print("\nList After Removing Duplicates:")
    print_linked_list(result)