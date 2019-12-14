"""
    1st: use space
    - use an extra array to store the references of nodes
    - reverse that array
    - print the array out

    Time    O(2N)
    Space   O(N)
    28 ms, faster than 43.08%
"""


class Solution(object):
    def printLinkedListInReverse(self, head):
        """
        :type head: ImmutableListNode
        :rtype: None
        """
        refs = []
        while head != None:
            refs.append(head)
            head = head.getNext()
        refs = refs[::-1]
        for x in refs:
            x.printValue()


"""
    2nd: recursion

    Time    O(2N)
    Space   O(N) recursion call stack takes space
    28 ms, faster than 43.08%
"""


class Solution(object):
    def printLinkedListInReverse(self, head):
        """
        :type head: ImmutableListNode
        :rtype: None
        """
        if head != None:
            self.printLinkedListInReverse(head.getNext())
            head.printValue()
