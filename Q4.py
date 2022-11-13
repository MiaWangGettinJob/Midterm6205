#Time Complexity O(N)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def insert(self, head, value):
        previous = None
        current = head
        inserted = False
        insertNode = ListNode(value)
        if value <= current.val:
            head = ListNode(value)
            head.next = current
        previous = current
        current = current.next
        while current:
            front = current.next
            if previous.val < value and current.val >= value:
                previous.next = insertNode
                insertNode.next = current
                inserted = True
            previous = current
            current = front
        if not inserted:
            previous.next = insertNode

def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next =  ListNode(6)
    head.insert(head, 5)
    print(head.next.next.next.next.val)

main()
