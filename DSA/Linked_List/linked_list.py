class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
        
class Linked_list:
    def __init__(self):
        self.head=None

    def insert_at_begining(self,data):
        node=Node(data, self.head)
        self.head=node

    def print(self):
        if self.head is None:
            print("linked list is empty")
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, )

if __name__ == '__main__':
    ll = Linked_list()
    ll.insert_at_begining(10)
    ll.insert_at_begining(15)
    ll.print