# link list

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def generate_link_list(l):
        header = ListNode(-1)
        it = header
        for e in l:
            it.next = ListNode(e)
            it = it.next
        return header.next

    @staticmethod
    def print_link_list(head):
        l = list()
        it = head
        while it:
            l.append(it.val)
            it = it.next
        print(l)