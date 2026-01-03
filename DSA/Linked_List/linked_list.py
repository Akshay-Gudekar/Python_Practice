# Represents an individual element (Node) in the Linked List
class Node:
    def __init__(self, data=None, next=None):
        self.data = data  # Stores the actual value
        self.next = next  # Stores the reference (pointer) to the next node


# Manages the collection of nodes
class LinkedList:
    def __init__(self):
        # The head points to the very first node in the list
        self.head = None

    # Traverses the list and prints it in a readable format: val1 --> val2
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            # Append " --> " only if there is a next node
            llstr += str(itr.data) + ' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    # Returns the total number of nodes in the list
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    # Adds a node at the very start (updates head)
    def insert_at_begining(self, data):
        # New node's next becomes the current head
        node = Node(data, self.head)
        self.head = node

    # Adds a node at the end of the list
    def insert_at_end(self, data):
        # If list is empty, new node becomes the head
        if self.head is None:
            self.head = Node(data, None)
            return

        # Traverse until the last node (where next is None)
        itr = self.head
        while itr.next:
            itr = itr.next

        # Link the last node to the new node
        itr.next = Node(data, None)

    # Inserts data at a specific index
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        # Stop at the node just before the target index
        while itr:
            if count == index - 1:
                # New node points to current node's next
                node = Node(data, itr.next)
                # Current node now points to new node
                itr.next = node
                break

            itr = itr.next
            count += 1

    # Removes a node at a specific index
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        # If removing the first node, just move head forward
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        # Stop at the node just before the one we want to delete
        while itr:
            if count == index - 1:
                # Skip the target node by linking to the one after it
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    # Wipes current list and populates it with values from a list
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    # Finds a specific value and inserts new data immediately after it
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        # Check if head is the target value
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                # Link new node to current next, then update current next
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next

    # Searches for a value and removes that node
    def remove_by_value(self, data):
        if self.head is None:
            return

        # If head contains the value, move head to the next node
        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        # Look ahead at the next node's data
        while itr.next:
            if itr.next.data == data:
                # Bypass the node containing the target data
                itr.next = itr.next.next
                break
            itr = itr.next


# Execution Block
if __name__ == '__main__':
    ll = LinkedList()
    # Testing string based operations
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.insert_at(1, "blueberry")
    ll.remove_at(2)
    ll.print()

    ll.insert_after_value("mango", "apple")
    ll.print()

    ll.remove_by_value("orange")
    ll.print()

    ll.remove_by_value("figs")  # Should do nothing as "figs" isn't present
    ll.print()

    # Emptying the list one by one
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()

    # Testing integer based operations
    ll.insert_values([45, 7, 12, 567, 99])
    ll.insert_at_end(67)
    ll.print()