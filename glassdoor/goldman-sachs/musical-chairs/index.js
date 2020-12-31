/*
    Given N and K, you start at the 1st chair and you move forward K steps, 
    and then you remove the chair where you stop at. Then you start again from the next chair.
    Which number remains til the end?

    Note: If you reach to the end, move to the first chair

    e.g.1
    
    N = 4, K = 2

    1 2 3 4
    * ^     start at 1, stop at 2, then we remove 2

    1 3 4
      * ^   start at 3, stop at 4, then we remove 4

    1 3
    * ^     start at 1, stop at 3, then we remove 3

    1       answer

    e.g.2
    N = 6, K = 4

    1 2 3 4 5 6
    *     ^     start at 1, stop at 4 , then we remove 4

    1 2 3 5 6
      ^   *     start at 5, stop at 2 , then we remove 2

    1 3 5 6
    ^ *         start at 3, stop at 1 , then we remove 1

    3 5 6
    *
    ^           start at 3, stop at 3 , then we remove 3

    5 6
    * ^         start at 5, stop at 6 , then we remove 6

    5           answer

    e.g.3
    N = 2, K = 2
    1 2
    * ^     start at 1, stop at 2, then we remove 2

    1       answer

    ref:
    - interview
*/
class ListNode {
    constructor(val=-1) {
        this.val = val
        this.next = null
    }
}

const musicalChairs = (N, K) => {
    // if (N <= 1 || K < 2) {
    //     return -1
    // }
    const head = new ListNode(1)
    let cur = head
    for (let i = 2; i <= N; i++) {
        cur.next = new ListNode(i)
        cur = cur.next
    }
    cur.next = head

    // _printList(head)
    cur = head
    while (cur.next != cur) {
        for (let i = 0; i < K-2; i++) {
            cur = cur.next
        }
        cur.next = cur.next.next
        cur = cur.next
        // _printList(head)
    }
    return cur
}

const _printList = (head) => {
    const res = []
    let cur = head
    while (true) {
        res.push(cur.val)
        cur = cur.next
        if (cur == head) break
    }
    console.log(res)
}

console.log(musicalChairs(4, 2))
console.log(musicalChairs(6, 4))
console.log(musicalChairs(2, 2))
console.log(musicalChairs(4, 3))
