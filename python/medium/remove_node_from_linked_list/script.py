class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pos=[]
        curr=head

        while(curr is not None):
            pos.append(curr)
            curr=curr.next

        if(len(pos)==1):
            head = None
        elif(len(pos)==n):
            head = head.next
        else:
            pos[len(pos)-n-1].next=pos[len(pos)-n-1].next.next
        return head

def main():
    sol = Solution()
    print(sol.removeNthFromEnd(ListNode(1,ListNode(2)), 2))

if __name__ == '__main__':
    main()