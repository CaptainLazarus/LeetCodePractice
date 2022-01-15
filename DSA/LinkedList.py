# from Typing import Optional

class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def display(head):
    temp = head
    while temp.next:
        print(temp.value)
        temp = temp.next
    print(temp.value)

head = ListNode(0)
temp = head
for i in range(1,10):
    # print(temp.value , i , temp.next)
    temp.next = ListNode(i)
    temp = temp.next

# print(head.value)
display(head)